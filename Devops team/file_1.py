def change_data(filepath, key, data):
    with open(filepath, "r") as f:
        lines = f.readlines()
        print(lines)
    
    with open(filepath, "w") as f:
        for line in lines:
            if key in line:
                f.write(f"{key}={data}\n")
            else:
                f.write(line)

change_data("data.txt", "password", "123333")

            
