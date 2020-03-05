{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def resize_pics(pics):\n",
    "    resize = []\n",
    "    for pic in pics:\n",
    "        resize.append(cv.resize(pic, (DIM, DIM)))\n",
    "    return np.array(resize)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_pics(path, lim = 1000): \n",
    "    pics = []\n",
    "    for i,pic in enumerate(os.listdir(path)):\n",
    "        gray = cv.cvtColor(cv.imread(path + pic), cv.COLOR_BGR2GRAY)\n",
    "        pics.append(gray)\n",
    "        \n",
    "        if i == lim:break\n",
    "    return pics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
