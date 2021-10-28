from runners.xiaogj_test_runner import TestRunner


class Main(object):

    @staticmethod
    def start_xiaogj_test():
        TestRunner().run()

if __name__ == "__main__":
    Main.start_xiaogj_test()