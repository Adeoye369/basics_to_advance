import time

content_size = 1234453
content_size_kb = f"{round(content_size/1024, 2) }"
done = downloaded = 0

while downloaded < content_size:
    chunk = content_size/100 # divided the file size evenly
    time.sleep(0.1)
    downloaded += chunk
    progress =f"[{'='*(int(done/2))}|({done+1}%){round(downloaded/1024, 2)}/{content_size_kb}kb]" 
    print(progress, end="\r")
    done += 1

    # Download is complete
    if downloaded >= content_size:
        print(progress)