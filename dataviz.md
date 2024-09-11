# Assignment: Visualizing government debt using Tableau
## Part 1: Working with web-based visualization tools and data
<img src="Part1.png" alt="Government Debt Bar Chart" width="700" />



## Part 2: Working with Tableau 
<div class='tableauPlaceholder' id='viz1725975588561' style='position: relative'><noscript><a href='#'><img alt='Part 2: OECD Data Set ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pa&#47;Part2OECDDataset&#47;Part2OECDDataSet&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Part2OECDDataset&#47;Part2OECDDataSet' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pa&#47;Part2OECDDataset&#47;Part2OECDDataSet&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                
<script type='text/javascript'>                  
  var divElement = document.getElementById('viz1725975588561');               
  var vizElement = divElement.getElementsByTagName('object')[0];                   
  vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                 
  var scriptElement = document.createElement('script');                  
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';               
  vizElement.parentNode.insertBefore(scriptElement, vizElement);                
</script>
(&nbsp;)
You can also explore the interactive **Debt-to-GDP Heat Map** using this [link to the Tableau visualization](https://public.tableau.com/views/Part3OECDDataset/Part2OECDDataSet?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link).


## Part 3: Create your own visualization
<div class='tableauPlaceholder' id='viz1725850514101' style='position: relative'><noscript><a href='#'><img alt='Debt-to-GDP Ratio Trends for North America &amp; Oceania (All)An interactive visualization showing the historical debt-to-GDP ratios of selected countries over time. Use the filters to explore different regions and years to compare trends in national debt le ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5M&#47;5MJHW7DT7&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;5MJHW7DT7' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5M&#47;5MJHW7DT7&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>              
<script type='text/javascript'>                   
  var divElement = document.getElementById('viz1725850514101');                   
  var vizElement = divElement.getElementsByTagName('object')[0];                   
  vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                   
  var scriptElement = document.createElement('script');                   
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                   
  vizElement.parentNode.insertBefore(scriptElement, vizElement);               
</script>
(&nbsp;)
You can also explore the interactive **Debt-to-GDP Ratio Trends by Country (1995–2019)** using this [link to the Tableau visualization](https://public.tableau.com/shared/W3DM6SR45?:display_count=n&:origin=viz_share_link).


## Comparing Visualization Methods

For this project, I experimented with three different ways of visualizing government debt-to-GDP ratios: a bar chart, a heat map, and a line graph. Each method provided a unique way to look at the data, and I’ll explain what worked, what didn’t, and why I ultimately went with the line graph as the most effective choice.

#### Part 1: Bar Chart:
The bar chart gave me a clear way to compare the debt-to-GDP ratios of different countries for one specific year—2018. It’s a very straightforward visualization, which made it easy to see which countries had the highest or lowest debt. For example, countries like Japan and Portugal stood out clearly. One feature I liked was that you could click on individual countries to isolate them, which helped focus the comparison. However, I did run into an issue with clutter—because there were so many countries, the labels on the X-axis became cramped, and some country names were missing entirely.. This affected how easy it was to interpret the chart quickly. Also, the bar chart only shows one year at a time, so it doesn’t let you see how debt levels changed over time, which felt limiting.

#### Part 2: Heat Map:
Next, I used a heat map, which gave me a bigger picture by showing debt levels across multiple years. The colors made it easy to spot overall patterns—countries like Japan and Italy had consistently high debt, while others stayed relatively low. This visualization was useful for seeing trends over time, which the bar chart couldn’t do. However, one problem I noticed was that it was harder to tell the exact values just by looking at the colors. For example, countries with similar debt levels were sometimes shaded almost the same, making it difficult to differentiate them. I think adding hover tooltips with the exact debt-to-GDP ratio for each country and year would make the heat map more precise. Overall, the heat map was great for spotting patterns but not for getting specific details.

#### Part 3: Line Graph:
I chose the line graph as my final visualization because it provided the most effective way to show how debt-to-GDP ratios change over time. One of the primary features I added was the option to choose specific years, whether it’s a single year, all years, or a custom selection of multiple years. This added flexibility allowed users to tailor the visualization based on what they wanted to compare, making the exploration of the data more targeted and useful. For instance, if someone wanted to analyze debt trends during a global recession or covid, they could easily select the relevant years and focus on those time periods.

In addition to this, I also segregated countries by region to further enhance flexibility and usability. By grouping countries into regions such as North America, Europe, or Asia, users could isolate specific areas of interest rather than having to scroll through a long list of countries. This feature made the line graph less overwhelming and allowed for a more organized comparison between regions. Users can now look at regional trends or select multiple regions to compare how different parts of the world have managed debt levels over time. Additionally, users can select individual countries from within a region, and the data for that country will be highlighted, making it easier to focus on specific comparisons within the broader regional context.

To improve clarity, I worked on creating a better, more descriptive title for the line graph. The new title immediately reflects the core of the data being visualized, ensuring that users can understand the chart’s purpose at a glance. Along with this, I included a short paragraph directly below the title that explains how to interact with the visualization. This paragraph guides users through the options for selecting regions, filtering years, and interacting with the graph. It ensures that even first-time users can easily navigate and make use of the interactive features without feeling confused.

One of the standout features I added was a dynamic title. This title updates based on the filters applied by the user, providing real-time context for what is being displayed. For example, if a user selects to view North America's and EU's debt ratios from 2000-2020, the title will adjust to reflect these parameters, making the chart more intuitive and clear. This dynamic feature helps users stay oriented as they explore different regions and time frames, ensuring they always know what data they’re looking at.

Finally, to make the graph even more user-friendly, I added country labels at the end of each line. This allows users to easily identify which line corresponds to each country without needing to cross-reference a separate legend. This simple addition reduces the cognitive load on users and ensures they can quickly understand the data without extra effort.

#### Conclusion
Each of the three visualization methods—bar chart, heat map, and line graph—brought something different to the table. The bar chart was simple and great for quick, single-year comparisons, while the heat map helped spot trends across multiple years. However, the line graph stood out as the best tool because it offered much more flexibility. By allowing users to choose specific years, compare regions, and providing clear, interactive titles, the line graph made it easier to dive deeper into the data. These features gave users control over what they wanted to explore, making the data not just easier to understand but also more engaging. Overall, the line graph gave the clearest picture of how debt-to-GDP ratios evolved over time and was the most helpful for identifying trends.

#### Data Source
OECD. (2024). OECD Data. OECD. Retrieved September 10, 2024, from https://www.oecd.org/en/data.html
