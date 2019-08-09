# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 08:47:45 2019

@author: csunj
"""CPC_HQ



import twint
import pandas as pd
import os
import nest_asyncio
nest_asyncio.apply()



# Configure
c = twint.Config()
c.Username = ""
c.Format = "Tweet id: {id} | Tweet: {tweet}"
c.Limit = 10

c.Store_csv = True
c.Output = "twitter"

# Run
twint.run.Search(c)