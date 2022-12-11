<?php
if(isset($_POST['submit'])) {
  // Get the uploaded file
  $file = $_FILES['fileToUpload'];

  // Check if the file is uploaded successfully
  if(is_uploaded_file($file['tmp_name'])) {
    // Set the target directory for the uploaded file
    $upload_dir = "uploads/";

    // Set a new file name for the uploaded file
    $new_file_name = time() . "_" . $file['name'];

    // Move the uploaded file to the specified directory
    if(move_uploaded_file($file['tmp_name'], $upload_dir . $new_file_name)) {
      echo "File uploaded successfully";
    } else {
      echo "Failed to move uploaded file";
    }
  } else {
    echo "Failed to upload file";
  }
}
?>

