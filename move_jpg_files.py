import os
import shutil

source_folder = "my_files"

destination_folder = os.path.join(source_folder, "jpg_files")

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):

        source_path = os.path.join(source_folder, filename)

          
        if filename.lower().endswith(".jpg"):

            destination_path = os.path.join(
                        destination_folder,
                        filename
                                            )

            shutil.move(source_path, destination_path)

            print("Moved:", filename)

            print("\nAll JPG files have been moved successfully!")