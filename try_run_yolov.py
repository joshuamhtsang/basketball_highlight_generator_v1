from ultralytics import YOLO

if __name__ == '__main__':

    # Load a model
    model = YOLO("yolov8n.yaml")  # build a new model from scratch
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

    # Use the model
    model.train(data="coco8.yaml", epochs=3)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set
    #results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
    results = model("C0012_10sec.MP4")
    
    for result in results:
        boxes = result.boxes
        result.save(filename="result.jpg")


    path = model.export(format="onnx")  # export the model to ONNX format

