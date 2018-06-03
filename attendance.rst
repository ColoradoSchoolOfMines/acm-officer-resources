Attendance
==========

:Owner: Jack Garner

Use the ACM Website has a built-in survey system to create a survey before each
meeting. Important data points to collect are:

- Name
- Is this your first time at ACM? If so, how did you hear about ACM?
- How did you find out about the event? (This is especially useful for tech
  talks.)

In addition to these, collect any other metrics you want. In general, make
everything except for name optional. We don't want people to skip filling out
the survey because they're overwhelmed by the number of fields that they have to
fill out.

Also, in the root of this repository there is the ``acm_membership.py`` script,
which can be useful in exporting a CSV of ACM members. It is important to upload
this CSV to http://www.acm.org/chapters/chapters/interface before April/May of
each year. This needs to be done as part of completing the Chapter Annual
Report. The process is relatively simple:

  - Login as an admin to http://acm.mines.edu
  - Get the value of the "authtkt" cookie
  - Run the script with arguments:

    - Cookie value
    - First survey id to consider
    - Last survey id to consider
    - Output CSV filename

  - After completing, the script will output a list of names that could not be
    resolved. Fix as many as possible without driving yourself crazy, and add
    them to the CSV.
  - Upload to http://www.acm.org

As of May 2018, the script works like a charm. The last survey processed for the
2017/2018 year was #26.
