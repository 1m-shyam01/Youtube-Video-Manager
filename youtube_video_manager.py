import json
def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
def list_all_videos(videos):
    print("\n")
    print("-"*70)
    for index, video in enumerate(videos,start=1):
        print(f"{index}. {video['name']} - Duration: {video['time']}")
        print("\n")
        print("-"*70)
def add_video(videos):
    name = input("Enter the name of the video : ")
    time = input("Enter video time : ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)
    
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video index to update: "))
    if 1<=index<=len(videos):
        name = input("Enter the new name of the video: ")
        time = input("Enter the new time of the video: ")
        videos[index-1] = {'name':name,'time':time}
        save_data_helper(videos)
    try:
        index = int(input("Enter the index of the video to update: "))
        if 1 <= index <= len(videos):
            name = input("Enter the new name of the video: ")
            time = input("Enter the new time of the video: ")
            videos[index-1] = {'name':name,'time':time}
            save_data_helper(videos)
        else:
            print("Invalid index. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")
def delete_video(videos):
    list_all_videos(videos)
    input_index = int(input("Enter the index of the video to delete: "))
    if 1 <= input_index <= len(videos):
        videos.pop(input_index-1)
        save_data_helper(videos)
    else:
        print("Invalid index. Please try again.")
def main():
    videos= load_data()
    while True:
        print("\n Youtube Video Manager | Choose an option:")
        print("\n Youtube Video Manager")
        print("1. List all youtube videos")
        print("2. add a youtube video")
        print("3. update a youtube video")
        print("4. delete a youtube video")
        print("5. Exit the application")
        choice = input("Enter your choice (1-5) : ")
        print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print("Exiting the application. Goodbye!")
                break
            case _:
                print("Invalid Choice")
if __name__ == "__main__":
    main()