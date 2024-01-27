import streamlit as sl
from pytube import YouTube
import re

sl.title("Download Youtube vid")
link = sl.text_input("Enter link of the video")

if link:
    vid = YouTube(link)
    sl.title(vid.title)
    sl.image(vid.thumbnail_url)

    sl.title("Video Formats")
    sl.subheader("mp4")
    ls=vid.streams.all()
    ls1=list((vid.streams.filter(file_extension='mp4')))
    resitag=[]
    counter=0
    for i in ls1:
       resitag.append(re.findall('\d{1,4}',str(i)))
    for i in range(0,len(ls1)):
         resitag[i]=resitag[i][0:3]
    selected = sl.selectbox("Select the quality of video/audio to download",resitag)
    # itag = re.findall('\d{1,4}',str(selected))
    but=sl.button("Download")
    if but:
        down=vid.streams.get_by_itag(int(selected[0]))
        down.download()
        
    