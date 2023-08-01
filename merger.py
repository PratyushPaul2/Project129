import pandas as pd
import numpy as np
star_df_1=pd.read_csv("/Desktop/Project127/updated_scraped_data.csv")
new_star_df_1=pd.read_csv("/Desktop/Project127/new_scraped_data.csv")
brightest_star_df=pd.read_csv("/Desktop/Project127/brightest_stars.csv")

headers = ["Star", "Constellation", "Right Ascension", "Declination", "App. Mag.", "Distance (ly)","Spectral Type","Brown Dwarf","Mass","Radius"]
final_star_df=pd.DataFrame(columns=headers)
final_star_df=pd.merge(star_df_1,new_star_df_1)

archive_star_df=pd.read_csv("/Desktop/Project127/final_scraped_data.csv")

archive_star_df["Star"]=archive_star_df["Star"].str.lower()
archive_star_df=archive_star_df.sort_values("Star")

archive_star_df["Radius"]=archive_star_df["Radius"]*0.102763
archive_star_df["Mass"]=archive_star_df["Mass"]*0.000954588

merge_stars_df=pd.merge(archive_star_df,,on="id")