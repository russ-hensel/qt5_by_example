

echo "The script is to copy files for qt_widget_by_example to its github location on my drive :"


cd  /mnt/WIN_D/Russ/0000/python00/python3/_projects/qt_by_example/

#cp  qt_sql_widgets.py   /mnt/WIN_D/for_github/qt_by_example/   -f
#
#/mnt/WIN_D/Russ/0000/python00/python3/_projects/qt_by_example/qt_sql_widgets.py
#
#
#/mnt/WIN_D/for_github/qt_by_example/test_target

# still need all of docs



ls
echo "hit any key to continue... "
read RESPONSE

rsync -u -t -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/qt5_by_example/*.*       /mnt/WIN_D/for_github/qt5_by_example
rsync -u -t -vv -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/qt5_by_example/docs/*.*  /mnt/WIN_D/for_github/qt5_by_example/docs
# ---- tabs
rsync -u -t -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/qt5_by_example/tabs/*.*                  /mnt/WIN_D/for_github/qt5_by_example/tabs
rsync -u -t -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/qt5_by_example/tabs/basic_widgets/*.*    /mnt/WIN_D/for_github/qt5_by_example/tabs/basic_widgets
rsync -u -t -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/qt5_by_example/tabs/basic_sql/*.*        /mnt/WIN_D/for_github/qt5_by_example/tabs/sql_widgets
rsync -u -t -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/qt5_by_example/tabs/book_fitz/*.*        /mnt/WIN_D/for_github/qt5_by_example/tabs/book_fitz
rsync -u -t -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/qt5_by_example/tabs/real_python/*.*      /mnt/WIN_D/for_github/qt5_by_example/tabs/real_python
rsync -u -t -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/qt5_by_example/misc/*.*                  /mnt/WIN_D/for_github/qt5_by_example/misc

# to libs ----------------------------------------------
rsync -u -t -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/rshlib/rshlib_qt/*.*     /mnt/WIN_D/for_github/qt5_by_example/libs

rsync -u -t -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/rshlib/in_spect/*.*         /mnt/WIN_D/for_github/qt5_by_example/libs
rsync -u -t -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/rshlib/app_services/*.*     /mnt/WIN_D/for_github/qt5_by_example/libs

rsync -u -t -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/stuffdb//key*.*             /mnt/WIN_D/for_github/qt5_by_example/libs

rsync -u -t -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/rshlib/string_util.py     /mnt/WIN_D/for_github/qt5_by_example/libs
# rsync -u -t -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/rshlib/app_*.py            /mnt/WIN_D/for_github/qt5_by_example/libs
rsync -u -t -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/rshlib/os_call.py            /mnt/WIN_D/for_github/qt5_by_example/libs




rsync -u -t -progress       /mnt/WIN_D/russ/0000/python00/python3/_projects/stuffdb/qsql_utils.py     /mnt/WIN_D/for_github/qt5_by_example/libs

#cp  theprofm_bku_here_to_l.sh     /mnt/WIN_D/for_github/qt_by_example/   -f
# cp  utils_for_tabs.py       /mnt/WIN_D/for_github/qt_by_example/   -f




# ---------------------





# here just wait for a keystroke ( or comment out )
echo "hit any key to continue and exit "
read RESPONSE


# --------------------- eof
