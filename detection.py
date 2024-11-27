import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from time import time

# Load model
model = load_model('best_model.h5')

# Define class names
class_names = ['karbohidrat', 'protein', 'sayur', 'buah', 'minuman']

def preprocess_image(image):
    image = cv2.resize(image, (224, 224))
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    return np.expand_dims(image, axis=0)

def get_region_proposals(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply blur and thresholding
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Get bounding boxes from contours
    regions = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        # Filter small regions
        if w > 50 and h > 50:
            regions.append((x, y, w, h))
    
    return regions

def detect_objects_in_region(image, box, min_confidence=0.5):
    x, y, w, h = box
    region = image[y:y+h, x:x+w]
    
    # Skip if region is too small
    if region.shape[0] < 32 or region.shape[1] < 32:
        return None
    
    processed_region = preprocess_image(region)
    predictions = model.predict(processed_region, verbose=0)
    confidence = float(np.max(predictions[0]))
    
    if confidence >= min_confidence:
        class_idx = np.argmax(predictions[0])
        return {
            'box': box,
            'confidence': confidence,
            'class': class_names[class_idx]
        }
    return None

def apply_nms(detections, nms_threshold=0.3):
    if not detections:
        return []
        
    boxes = [d['box'] for d in detections]
    scores = [d['confidence'] for d in detections]
    
    # Convert boxes to the format expected by NMSBoxes
    boxes_nms = [[b[0], b[1], b[0] + b[2], b[1] + b[3]] for b in boxes]
    
    indices = cv2.dnn.NMSBoxes(boxes_nms, scores, 0.5, nms_threshold)
    
    return [detections[i] for i in indices.flatten()]

def draw_detection(image, detection):
    colors = {
        'karbohidrat': (255, 0, 0),    # Blue
        'protein': (0, 255, 0),         # Green
        'sayur': (0, 0, 255),           # Red
        'buah': (255, 255, 0),          # Cyan
        'minuman': (255, 0, 255)        # Magenta
    }
    
    x, y, w, h = detection['box']
    class_name = detection['class']
    confidence = detection['confidence']
    color = colors.get(class_name, (0, 255, 0))
    
    # Draw bounding box
    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
    
    # Draw label
    label = f'{class_name}: {confidence:.2f}'
    (label_w, label_h), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    cv2.rectangle(image, (x, y - label_h - 5), (x + label_w, y), color, -1)
    cv2.putText(image, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

def process_frame(frame, max_regions=10):
    # Get region proposals
    regions = get_region_proposals(frame)
    
    # Limit number of regions for performance
    regions = regions[:max_regions]
    
    # Detect objects in regions
    detections = []
    for box in regions:
        result = detect_objects_in_region(frame, box)
        if result:
            detections.append(result)
    
    # Apply NMS
    detections = apply_nms(detections)
    
    # Draw detections
    for det in detections:
        draw_detection(frame, det)
    
    return frame

def detect_objects(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not read image")
    
    start_time = time()
    processed_image = process_frame(image.copy())
    print(f"Processing time: {time() - start_time:.2f} seconds")
    
    return processed_image

def realtime_detection():
    cap = cv2.VideoCapture(0)
    fps_time = time()
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Process frame
        processed_frame = process_frame(frame)
        
        # Calculate and display FPS
        frame_count += 1
        if frame_count >= 30:
            fps = frame_count / (time() - fps_time)
            print(f"FPS: {fps:.2f}")
            frame_count = 0
            fps_time = time()
        
        # Display result
        cv2.imshow('Food Detection', processed_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def main():
    print("Choose detection mode:")
    print("1. Image detection")
    print("2. Real-time detection")
    
    choice = input("Enter your choice (1 or 2): ")
    
    try:
        if choice == '1':
            image_path = input("Enter image path: ")
            result = detect_objects(image_path)
            
            plt.figure(figsize=(10, 10))
            plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.show()
        
        elif choice == '2':
            realtime_detection()
        
        else:
            print("Invalid choice!")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
