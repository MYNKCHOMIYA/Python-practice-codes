j =2
for i in range(2,22):
            with open(f"tables/{i}.txt","w") as f:
                            for j in range(1,11):
                                 f.write(f"{i} x {j}= {i*j}\n")
                     