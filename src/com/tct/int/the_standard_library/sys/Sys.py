import sys

if __name__ == '__main__':

    sys.path.append('/local/tools_int/lib')
    print sys.byteorder
    # print sys.argv
    # print sys.copyright

    print sys._current_frames
    print sys.getdefaultencoding()
    # print sys.setdefaultencoding()

    for i in sys.path:
        print i

    # print sys.api_version

    print sys.platform
    print sys.getsizeof('1z1')
    print sys.getprofile()
    print sys.getwindowsversion
