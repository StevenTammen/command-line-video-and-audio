### Folder structure

- content-page/
  - _index.md
  - image1.jpg
  - ...
  - segments.xlsx
  - video.mp4
  - audio.mp3
  - recording/
    - raw/
        - 10.mp4
        - 20.mp4
    - processed/
        - 10-processed.mp4
        - 20-processed.mp4
    - topic-transitions/
        - 10-20-transition.mp4
        - 20-30-transition.mp4

### Concatenating video with ffmpeg

* [concatenate videos ffmpeg - Google Search](https://www.google.com/search?q=concatenate+videos+ffmpeg&sca_esv=ca43310e5c28fa02&sxsrf=AM9HkKmYdYq95vyhUjViM_US00Nrs6ULKA%3A1699302605620&ei=zUxJZfq8JaGIwbkP4qqsiAg&ved=0ahUKEwi617HBm7CCAxUhRDABHWIVC4EQ4dUDCBA&uact=5&oq=concatenate+videos+ffmpeg&gs_lp=Egxnd3Mtd2l6LXNlcnAiGWNvbmNhdGVuYXRlIHZpZGVvcyBmZm1wZWcyBBAjGCcyCBAAGIoFGJECMgYQABgWGB4yBhAAGBYYHki_BlDnA1idBXABeAGQAQCYAXOgAeYBqgEDMC4yuAEDyAEA-AEBwgIKEAAYRxjWBBiwA-IDBBgAIEGIBgGQBgg&sclient=gws-wiz-serp)
* [Concatenating Videos Using FFmpeg | Baeldung on Linux](https://www.baeldung.com/linux/ffmpeg-video-concatenation)
* [Concatenate – FFmpeg](https://trac.ffmpeg.org/wiki/Concatenate)
* [How to Merge Video Files Using FFmpeg - Bannerbear](https://www.bannerbear.com/blog/how-to-merge-video-files-using-ffmpeg/)
* [ffmpeg concat demuxer with file without audio stream“concat” Demuxer site:superuser.com - Google Search](https://www.google.com/search?q=ffmpeg+concat+demuxer+with+file+without+audio+stream%E2%80%9Cconcat%E2%80%9D+Demuxer+site:superuser.com&sca_esv=ca43310e5c28fa02&sxsrf=AM9HkKlXQoKWjFOjr3sxgomNtjvYLsvysw:1699303219132&sa=X&ved=2ahUKEwjUtPflnbCCAxXSgYQIHajDB2EQrQIoBHoECBcQBQ&biw=1912&bih=932&dpr=1)
* [Use FFMpeg concat demuxer with multiple files with/without audio tracks - Super User](https://superuser.com/questions/1624249/use-ffmpeg-concat-demuxer-with-multiple-files-with-without-audio-tracks)
* [Merging several videos with audio channel and without audio - Super User](https://superuser.com/questions/1044988/merging-several-videos-with-audio-channel-and-without-audio/1044997#1044997)
* [ffmpeg - Adding audio to picture: video too long even when using -shortest - Video Production Stack Exchange](https://video.stackexchange.com/questions/27738/adding-audio-to-picture-video-too-long-even-when-using-shortest/27740#27740)
* [Concatenate videos with/without audio stream - Super User](https://superuser.com/questions/928770/concatenate-videos-with-without-audio-stream?rq=1)


### Structure of segments.xlsx Excel file

The tab titled 'Initial' is what is synced with headers from content section. It does not represent actual titles used for segments; it needs cleaning up. Some segments may be added to headers from page ("Intro", "Outline", "Summary", "Outro", etc.), and not every header from the content will have its own segment.
   
The tab titled 'Full' is the one representing the true list of segments. It also contains the dud indicator, timestamps, internal timestamps, and so on

### Checking timestamps locally (before upload combined video/ripped audio to platforms)

Want some way to verify timestamp accuracy locally, before uploading files to platforms/potentially having to undo that step if something turns out to be amiss.

In doing this verification, we want something fast and keyboard-driven. The equivalent of this feature on YouTube:

* [Are there YouTube keyboard shortcuts for moving forward and backward through a video's chapters? - Web Applications Stack Exchange](https://webapps.stackexchange.com/questions/143429/are-there-youtube-keyboard-shortcuts-for-moving-forward-and-backward-through-a-v)

VLC can do this with video chapters:

- Shift + N : Next chapter
- Shift + P : Previous chapter
- See [this video](https://www.youtube.com/watch?v=KO2TnlEP9Rg) for chapters in VLC generally. I automate making them with Python and ffmpeg, but it's the same idea as making them manually here with Drax.

* [How do you add chapters to a video file? : r/VideoEditing](https://www.reddit.com/r/VideoEditing/comments/p3fc61/how_do_you_add_chapters_to_a_video_file/)
* [How to Add Chapters to MP4s with FFmpeg - Kyle Howells](https://ikyle.me/blog/2020/add-mp4-chapters-ffmpeg)

Before thinking of video chapters and the keyboard shortcuts to go from one to the next (which is definitely best, in my opinion---which is why I dumped my other ideas and went with that one once I'd thought of it), I had been looking for a way to replicate the hyperlinks of the timestamp list in the YouTube video description.

After learning you could run a shell command to go to a specific location in VLC (e.g., [here](https://www.reddit.com/r/VLC/comments/pixxm3/start_a_video_at_a_specific_time/)), I'd thought maybe I could set up hyperlinks in Excel to jump to sections in the timestamp list. Since I'm already writing the timestamps to to Excel via Pandas anyway, maybe I could just make the timestamps links in that way?

It turns out that hyperlinks in Excel are somewhat restricted. If you want to support command line commands (with arguments and so on), you need a VBA macro for it:

* [Execute Shell Commands from Excel Cell - Super User](https://superuser.com/questions/1220696/execute-shell-commands-from-excel-cell)
* [Excel Hyperlinks Run Command Files - Contextures Blog](https://contexturesblog.com/archives/2017/09/14/excel-hyperlinks-run-command-files/)

Adding macros to workbooks generally:

* [How to Add Macro Code to Excel Workbook](https://www.contextures.com/xlvba01.html)

But adding macros requires the file to be .xlsm, not .xlsx. And openpyxl and xlsxwriter (two packages commonly used with pandas to write dataframes to Excel) don't support dealing with macros in Python programmatically:

* [python - How write to xlsm using openpyxl - Stack Overflow](https://stackoverflow.com/questions/49470871/how-write-to-xlsm-using-openpyxl)
* [python - How to save XLSM file with Macro, using openpyxl - Stack Overflow](https://stackoverflow.com/questions/17675780/how-to-save-xlsm-file-with-macro-using-openpyxl)

Like, I think you might be able to open/edit the sheets in an .xlsm file, but doesn't look like openpyxl lets you programmatically add macros? (I would need to do that in creating the workbook for the first time, to support the special hyperlinks that let run stuff via shell commands).

I think another package called xlwings could interface with dataframes from pandas, and I think better supports macros:

* [Quickstart - xlwings Documentation](https://docs.xlwings.org/en/stable/quickstart.html)
* [python - Exporting a pandas dataframe to excel using xlwings - Stack Overflow](https://stackoverflow.com/questions/74308632/exporting-a-pandas-dataframe-to-excel-using-xlwings)

I didn't look too far into this, since it was at about this point in the research process I thought to check video chapters. But it does seem like it ought to work.

It also looks like you can us xlwings as the glue to link Python to Excel for further automation:

* [Python makes spreadsheets Excel’lent | by Vinayak Nayak | Towards Data Science](https://towardsdatascience.com/python-makes-spreadsheets-excellent-f48ce0c648e3)

I may look into that more at some point. Although now that [Python in Excel](https://support.microsoft.com/en-us/office/introduction-to-python-in-excel-55643c2e-ff56-4168-b1ce-9428c8308545#:~:text=Python%20in%20Excel%20brings%20the,are%20returned%20to%20the%20worksheet.) is a thing, maybe it won't bee needed any more?





-----

### TODO: clean up and write better

First step should be to check all the things that could possible cause errors, and then short-circuit if any of these fail. So that errors do not cause any confusing partial completion state. Also simpler than that getting partway and then writing code to roll back (like transactions in databases).

That would work, but short-circuiting is just easier; it is less effort overall, since there is nothing to roll back if you don't do anything until you know all the operations will work.

So, things to test upfront:

- Does the number of raw files match the number of rows in the 'Full' tab of the segments spreadsheet? (Duds do not throw off, if tracked properly)
  - If GoPro case, does the number of recordings (rather than partials) line up? That case makes the checking a bit harder
- Test any external dependencies upfront, like ffprobe. So that if config isn't set up right for some reason, gets caught upfront, before anything is
done = state gets altered
- (Temporary for right now): are there N - 1 topic transition segments?
  - Eventually will build these automatically, rather than having to record and have this room for human error, also costing extra effort

  


Should be able to run the timestamp-generation separately from video processing stuff to update the content file and YouTube description post-hoc, to ensure standardization in approach. Going back and adding timestamp links to all the headers corresponding to segments is the big reason for this. So that doesn't have to get done manually. Once that bit is done, all future things will do it implicitly, but then still have to do it for things that had already been done.




Uploading is a separate step, since one needs to verify the video file (check timestamps), before uploading it. To avoid rework and deleting/re-uploading, and other hassle if things are wrong.

Also short circuit on things related to publishing upfront

- Does content file have playlist in frontmatter?
- Does content file have summary?

After have video and timestamps, check timestamps using VLC command-line argument, to make going to timestamps comparable in speed to YouTube timestamp hyperlinks

https://apple.stackexchange.com/questions/411840/how-can-you-open-a-video-on-your-desktop-at-a-specific-time-using-terminal

Whether make links in Excel, type things in on command line, or whatever, try to find fastest option, so that it really is comparable time-wise to just clicking timestamp hyperlinks. Having soemthing that is actually a hyperlink that would be preferable to having to type in the timestamp, or copy-paste a full command from Excel into a terminal.

* [Execute Shell Commands from Excel Cell - Super User](https://superuser.com/questions/1220696/execute-shell-commands-from-excel-cell)
* [Excel Hyperlinks Run Command Files - Contextures Blog](https://contexturesblog.com/archives/2017/09/14/excel-hyperlinks-run-command-files/)



Improvements to be made:

- Automating removal of silence, rather than having to babysit savvycut
- Automating creation of topic transition slides
- Automating merging of files, rather than having to manually do it through LosslessCut

- Automating adding video embed link and timestamps to content file, and the 
re-triggering preprocessor to get in aggregation page and so on too
- Automating creation of YouTube description

- Automating upload to YouTube
- Automating upload to podcast platforms
- Automating upload to Archive.org
