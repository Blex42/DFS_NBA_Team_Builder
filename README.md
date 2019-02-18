![Blex Image](https://yt3.ggpht.com/-JRwX7pOt8nk/AAAAAAAAAAI/AAAAAAAAAAA/WIuQ1Zm0J5k/s88-c-k-no-mo-rj-c0xffffff/photo.jpg)



**DFSNBA_Team_Builder**

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/Blex42)

**Install**

`pip install DFSNBA-TeamBuilder`


Pandas is needed to import and export the offical draftkings file

```python
import pandas as pd

##This is the actual package that you just downloaded
import DFS_NBA_Team_Builder 
from DFS_NBA_Team_Builder import DK_TeamBuilder

```

Set the variables

**Import the draftkings file**

```python
dfr=pd.read_csv("ExampleDKFile.csv")#This is the example file from GitHub
```

Set how many players you want to sample

**1 is no sampling 0 remove alls players .20 leaves you 20% of the players
#from the dk file**

```python
samplepercent= .20
```
**How many teams do you want to create**

```python
dkteams =20
```

**Use this exact function to call and create you lineups**

```python
playerusage, dkupload= DFS_NBA_Team_Builder.DK_TeamBuilder.DK_TeamBuildermod(dfr,dkteams,samplepercent)
```

This gives you a breakdown of how often you use players you many choose

to resample if you dont like how it looks

```python
playerusage.head()
```


</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>AvgPointsPerGame</th>
    </tr>
    <tr>
      <th>Name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>J.J. Barea</th>
      <td>12</td>
      <td>23.26</td>
    </tr>
    <tr>
      <th>Victor Oladipo</th>
      <td>11</td>
      <td>37.56</td>
    </tr>
    <tr>
      <th>Caris LeVert</th>
      <td>10</td>
      <td>30.72</td>
    </tr>
    <tr>
      <th>Tim Hardaway Jr.</th>
      <td>7</td>
      <td>29.48</td>
    </tr>
    <tr>
      <th>Blake Griffin</th>
      <td>7</td>
      <td>46.60</td>
    </tr>
  </tbody>
</table>
</div>



**This is the file that you actually upload into the draftkings website**
```python
dkupload.to_csv("DkTeamsUpload.csv")
```




**Purpose**

Create optimized NBA draftkings lineups with sampling

**What to do high level**

1.Import Draftkings Upload File [DK_Upload_Page](https://www.draftkings.com/lineup/upload)

2.Build a team or teams based on the amount of teams and amount of sampling you want

3.Use Linear Programming to optimze the teams for the maximum amount of points while staying under the salary cap


**End Notes**

This package was created to use the draftkings lineup file for any given night and run an optimization function on it in order to create the most efficient teams based on the average points columns. 


[GitHub_Repo](https://github.com/Blex42/DFS_NBA_Team_Builder)

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/Blex42)