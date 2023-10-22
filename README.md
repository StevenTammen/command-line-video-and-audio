
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


### Structure of segments.xlsx Excel file

The tab titled 'Initial' is what is synced with headers from content section. It does not represent actual titles used for segments; it needs cleaning up. Some segments may be added to headers from page ("Intro", "Outline", "Summary", "Outro", etc.), and not every header from the content will have its own segment.
   
The tab titled 'Full' is the one representing the true list of segments. It also contains the dud indicator, timestamps, internal timestamps, and so on
   




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
