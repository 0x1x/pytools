import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(handler)
logger.addHandler(console)

def ckDellZeroAllfiles(rootpath, topdown=False):
    logger.info('Start...')
    for root, dirs, files in os.walk(rootpath, topdown):
        logger.info("Now in PATH:"+root)
        for name in files:
            pathfile = os.path.join(root, name).replace('\\', '/')
            if os.path.getsize(pathfile) == 0:
                os.remove(pathfile)
                # logger.info("【file】Deleted:"+pathfile)
        if not os.listdir(root):
            os.rmdir(root)
            # logger.info("【dir】Deleted:"+str(root))
    logger.info('success!!!')


if __name__ == '__main__':
    p=input("Please input a path:")
    # logger.info("you input path is:"+p)
    ckDellZeroAllfiles(p)
    print("all ok")
