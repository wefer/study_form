#!/usr/bin/env python

import pandas as pd
from shutil import copyfile


def make_bkp(xlsfile):
	"""
	Make a copy of file.
	"""
	bkp_name = xlsfile + '.bkp'
	copyfile(xlsfile, bkp_name)


def write_to_xlsfile(content_df, xlsfile):
	"""
	Write a new dataframe line to excel file.
	"""
	print(content_df)
	df = pd.read_excel(xlsfile)
	df2 = df.append(content_df, ignore_index=True)
	make_bkp(xlsfile)
	order = content_df.columns
	df2 = df2[order]
	print('Writing to file: {}'.format(xlsfile))
	df2.to_excel(xlsfile, index=False)
