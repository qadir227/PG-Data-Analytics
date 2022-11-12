# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
dataset = pd.read_csv('matches.csv')


from dataprep.eda import create_report
create_report(dataset).show_browser()