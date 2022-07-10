import os

def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            print path
        else:
            walk(path)

print walk("C:\Users\kerem\OneDrive\Masaüstü\Masaüstü\Þehir University License\Year 1-2\Programming Practice\Deneme")
