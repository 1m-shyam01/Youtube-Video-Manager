
# YouTube Video Manager (Python Console App)

This is a small Python console project I made to practice **file handling**, **functions**, and **basic CRUD operations** (Create, Read, Update, Delete).  
The app lets me manage a list of YouTube videos (name and duration) and saves the data into a JSON file called `youtube.txt`.

---

## Features

- **List all videos**: Show all saved YouTube videos with their index, name, and duration.
- **Add a video**: Enter a video name and its time (for example, `10:35`) and save it.
- **Update a video**: Choose a video by its index and change its name and/or time.
- **Delete a video**: Remove a video from the list by index.
- **Save to file**: Data is stored in `youtube.txt` using JSON so it stays saved even after closing the app.

---

## How the project works

- The function `load_data()` tries to read the `youtube.txt` file and load the data using `json.load()`.  
  - If the file does not exist, it returns an empty list `[]`.
- The function `save_data_helper(videos)` saves the `videos` list back to `youtube.txt`.
- The program shows a menu in a loop:
  1. List all YouTube videos  
  2. Add a YouTube video  
  3. Update a YouTube video  
  4. Delete a YouTube video  
  5. Exit the application  

Based on my input, it calls the correct function using a `match` statement.

---

## How to run the project

1. Make sure you have **Python 3.10+** installed (because I used the `match` statement).
2. Open a terminal / command prompt in this folder.
3. Run the script:

   
