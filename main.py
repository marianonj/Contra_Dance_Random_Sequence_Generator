import sys
import DanceClasses
import wx





def setup():
    platform = sys.platform
    if platform == 'win32':
        from win32api import GetSystemMetrics
        width, height = GetSystemMetrics(0), GetSystemMetrics(1)
        print('b')



    print('b')
    return 0

def main():
    vars = setup()
    dancers = DanceClasses.return_starting_dancers(becket=False)
    pass

if __name__ == '__main__':
    main()