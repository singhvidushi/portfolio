# Assignment: Critique by Design with Tableau (MakeoverMonday)
## Step 1: Choose a data visualization from MakeoverMonday
[Generative AI Search Trends in the United States](https://trends.google.com/trends/explore?date=2022-01-01%202024-02-16&geo=US&q=Midjourney,Stable%20Diffusion,DALL%20E&hl=eng)
Souce: Google Trends

#### Why:
I chose the "Generative AI Search Trends in the United States" visualization from Google Trends because it highlights the growing interest in popular AI image generation tools across different U.S. regions. This topic is timely and relevant as AI tools continue to transform creative industries.
- MidJourney,
- Stable Diffusion, and
- DALL-E

The visualization's use of a geographic map and bar chart allows for quick comparisons, but there are opportunities for improvement in displaying detailed comparisons, enhancing interactivity, and addressing accessibility. These factors make it a compelling choice for a thoughtful critique and redesign.

## Step 2: Critique the data visualization
<table>
  <tr>
    <th>Heuristic</th>
    <th>What I Like</th>
    <th>What I Dislike</th>
    <th>What I Wish I Saw</th>
    <th>Score (Out of 10)</th>
  </tr>
  <tr>
    <td><strong>Usefulness</strong></td>
    <td>The area map cleanly represents state-by-state interest in AI image generation tools. The bar graph is easy to read, and the distinct colors make differentiating between tools straightforward. <br><strong>Why:</strong> This matches the usefulness heuristic by providing a clear overview of how each state’s interest is distributed. By using simple, distinct visuals, the data becomes actionable for stakeholders like marketers or developers wanting to know which regions favor certain tools.</td>
    <td>The map gives the impression that only one tool is in use per state (e.g., North Dakota and West Virginia are highlighted in yellow). This hides the fact that all three tools are being used in those states, which reduces insight. <br><strong>Why:</strong> This breaks the truthfulness heuristic by oversimplifying the data. It doesn’t show the full picture of usage for each tool and misleads the user into thinking one tool is dominant without showing the scale of dominance.</td>
    <td>A stacked bar graph directly on the map or an overlapping representation of tool usage in each state.<br><strong>Why:</strong> This would improve completeness and truthfulness, giving a more nuanced and accurate representation of tool usage rather than just highlighting the majority tool. It would also improve usefulness by offering more granular insights, making the data more actionable.</td>
    <td>7</td>
  </tr>
  <tr>
    <td><strong>Completeness</strong></td>
    <td>The visualization gives a clear overview of which tools are preferred in different states, based on search interest.<br><strong>Why:</strong> This meets the completeness heuristic by providing relevant, understandable information. The map gives a useful high-level breakdown, and the bar graph adds detail to help users compare between states.</td>
    <td>The x-axis of the bar graph doesn’t display percentages unless you hover over the bars, making it difficult to compare states at a glance. Additionally, the map doesn’t provide a detailed breakdown for each tool in a state, which could confuse users.<br><strong>Why:</strong> This violates the perceptibility heuristic because users cannot easily see the precise distribution of interest for each tool. It also violates completeness, as the lack of easily accessible data on the map and bar graph means users miss out on important details.</td>
    <td>Percentages labeled directly on the bars and tooltips on the map that show all three tools' percentages for each state, not just the majority one.<br><strong>Why:</strong> This would improve completeness by showing all relevant data, not just the dominant tool, and would enhance perceptibility by making comparisons easier without hovering. Users could quickly compare percentages between states or tools without extra effort.</td>
    <td>6</td>
  </tr>
  <tr>
    <td><strong>Perceptibility</strong></td>
    <td>The clean and simple design of the area map and bar graph makes it easy to follow visually.<br><strong>Why:</strong> This satisfies the perceptibility heuristic by displaying data in a clear, easy-to-read format, allowing users to quickly scan and absorb the information.</td>
    <td>The pop-up tooltip that appears when you hover over a state blocks the state name, making it difficult to identify the state. Additionally, the blue and yellow color scheme implies that only one tool dominates each state, even though multiple tools are in use.<br><strong>Why:</strong> This goes against perceptibility because the tooltip disrupts users' ability to identify states clearly. It also violates truthfulness by implying single-tool dominance and misleading users who want to understand the full usage within each state.</td>
    <td>A tooltip that doesn’t block the state name and a color gradient (or pie chart overlay) to show how each tool is used in every state.<br><strong>Why:</strong> This would improve perceptibility by making the data easier to access without obscuring essential information (state names). It would also boost truthfulness by showing a proportional breakdown of tool usage in each state, rather than suggesting one tool dominates.</td>
    <td>5</td>
  </tr>
  <tr>
    <td><strong>Truthfulness</strong></td>
    <td>The data seems accurate in highlighting the most popular tool in each state in Bar Chart.<br><strong>Why:</strong> This aligns with the truthfulness heuristic, as the data is presented reliably and reflects actual search interest.</td>
    <td>The map gives the impression that only one tool is in use per state (e.g., North Dakota and West Virginia are highlighted in yellow). This hides the fact that all three tools are being used in those states, which reduces insight.<br><strong>Why:</strong> This misrepresentation violates truthfulness by oversimplifying the data. Users can’t see the scale of usage for the other tools, leading to an inaccurate understanding of the tool landscape.</td>
    <td>More nuanced visual cues (e.g., stacked bars or proportional circles) to show that multiple tools are being used in each state. Also, percentages visible on the bar chart without needing to hover.<br><strong>Why:</strong> This would ensure truthfulness and perceptibility by showing a fuller, more accurate picture of tool usage across states and making comparisons clearer.</td>
    <td>6</td>
  </tr>
  <tr>
    <td><strong>Intuitiveness</strong></td>
    <td>The overall layout is intuitive, with clear labels and distinct colors for each tool.<br><strong>Why:</strong> This meets the intuitiveness heuristic because the map and bar chart are familiar formats that make it easy for users to navigate and understand.</td>
    <td>The bar graph always places MidJourney at the top, even when other tools are selected for comparison. This makes it harder to compare the data for the other tools.<br><strong>Why:</strong> This breaks the intuitiveness heuristic by adding unnecessary cognitive load. The user expects the graph to re-sort when they select a tool for comparison, but it doesn’t, making it more difficult to focus on the tool of interest.</td>
    <td>Dynamically sorted bar charts based on the tool selected, and more accessible details when hovering over the bar graph.<br><strong>Why:</strong> This would improve intuitiveness and usefulness, allowing users to quickly and easily compare interest in each tool without unnecessary effort or confusion.</td>
    <td>7</td>
  </tr>
  <tr>
    <td><strong>Aesthetics</strong></td>
    <td>The design is clean and simple, making it easy to focus on the data. The distinct colors—blue, red, and yellow—are clear and immediately help in distinguishing between the different tools. At first glance, the visualization is straightforward and doesn't overwhelm you with too much information. <br><strong>Why:</strong>  This works because it keeps the visualization uncluttered and helps users focus on what’s important without getting lost in unnecessary details.</td>
    <td>The solid colors used for the states feel a bit too rigid and flat, especially since they only highlight one tool per state. It doesn't show how much more one tool is preferred over the others, which takes away from the depth of the data.<br><strong>Why:</strong> Without using a more detailed color palette, the map doesn’t fully capture the differences in interest levels. It ends up feeling a bit static, which might make it less engaging for users who want to explore more nuances.</td>
    <td>I’d love to see more variation in the colors—maybe gradients or shading—that could reflect tool dominance in a more dynamic way. Adding some texture or changes in the bar graph design would also help make it more engaging and visually interesting.<br><strong>Why:</strong> This would improve both the look and feel of the visualization. It would make the data more engaging and accessible, while still keeping everything clear and easy to understand.</td>
    <td>6</td>
  </tr>
  <tr>
    <td><strong>Engagement</strong></td>
    <td>The area map and bar graph are engaging, providing users with multiple ways to explore the data.<br><strong>Why:</strong> This meets the engagement heuristic by inviting users to interact with the visualization in a way that leads to understanding, encouraging them to explore different states and tools.</td>
    <td>The map’s tooltip blocks state names, and percentages in the bar graph are only visible on hover. This makes it harder for users to quickly engage with the data.<br><strong>Why:</strong> This breaks engagement and perceptibility heuristics by making users work harder to access the data they need. It discourages deeper interaction and exploration.</td>
    <td>A more interactive experience with filters on the map, tooltips that don’t block state names, and visible percentages on the bar graph.<br><strong>Why:</strong> This would improve engagement by allowing users to explore the data more seamlessly and enhancing perceptibility by making key data points (like percentages) immediately available.</td>
    <td>7</td>
  </tr>
</table>

### Comparison of Stephen Few's Data Visualization Effectiveness Profile vs. Good Charts Method

In my critique, I used a combination of **Stephen Few's Data Visualization Effectiveness Profile** and the **Good Charts method** to get a well-rounded evaluation.

Stephen Few's method focuses on seven criteria: usefulness, completeness, perceptibility, truthfulness, intuitiveness, aesthetics, and engagement, providing a detailed, structured breakdown of the visualization's effectiveness. While, the Good Charts method is simpler and revolves around three key questions: What I like, What I dislike, and What I wish I saw. It offers a quicker, more subjective approach to evaluating the visualization.

#### Key Differences:
1. **Depth of Analysis**: Few's method provides a granular breakdown of the visualization's strengths and weaknesses, while Good Charts offers high-level, actionable feedback.
2. **Audience Needs**: Few's approach emphasizes understanding the target audience and ensuring the visualization meets their needs. Good Charts is more subjective but quicker to implement.
3. **Emotional Impact**: Few evaluates aesthetics and engagement explicitly, ensuring the visualization both informs and emotionally resonates, while Good Charts focuses more on functionality.

I used a blend of both methods to ensure a **comprehensive critique**, blending Few’s in-depth analysis with the quick, actionable insights of Good Charts. This provided a balanced evaluation that covered both **strategic depth** and **efficient insight** into what worked and what needed improvement.

## Step 3: Sketch out a solution
#### Map Sketch
<img src="Sketch.jpg" alt="Handdrawn1" width="700" />

I created the map sketch to provide a clearer representation of AI tool usage across states by incorporating proportional overlays or color gradients. This addresses the issue of the original map showing only the dominant tool in each state, which oversimplified the data. By allowing users to see multiple tools' usage in each state, the map sketch provides a more accurate and truthful visual representation.

#### Bar Graph Sketch
<img src="Sketch 2.jpg" alt="Handdrawn2" width="700" />

I created the bar graph sketch to improve data comparison by including stacked bars that show the proportion of interest for each tool within a state. This allows for a side-by-side comparison without needing to hover for details, improving user engagement and ease of use. 

## Step 4: Test the solution
<table>
  <tr>
    <th>Question</th>
    <th>late 20s, Student</th>
    <th>mid 40s, Engineer</th>
  </tr>
  <tr>
    <td><strong>Can you tell me what you think this is?</strong></td>
    <td>A visualization showing search trends for different AI tools across U.S. states with a map and a bar chart for comparison.</td>
    <td>A comparison of search interest for AI image generation tools across the United States using a map for geographical trends and a bar chart for more detailed breakdown.</td>
  </tr>
  <tr>
    <td><strong>Can you describe what this is telling you?</strong></td>
    <td>It's showing the popularity of AI tools like MidJourney, DALL-E, and Stable Diffusion in different regions.</td>
    <td>It shows which AI tools are most popular in various U.S. states, with the bar chart providing more specific comparisons.</td>
  </tr>
  <tr>
    <td><strong>Is there anything you find surprising or confusing?</strong></td>
    <td>The map is confusing as it only shows the dominant tool and hides the fact that multiple tools are in use.</td>
    <td>The map is misleading since it suggests only one tool is used per state. The bar chart not dynamically reordering by the selected tool is also surprising.</td>
  </tr>
  <tr>
    <td><strong>Who do you think is the intended audience for this?</strong></td>
    <td>People interested in AI trends like marketers, developers, or students studying AI or data visualization.</td>
    <td>AI developers, marketers, or analysts looking to understand regional trends, and companies targeting specific regions for AI tool promotion.</td>
  </tr>
  <tr>
    <td><strong>What part of the visualization do you find most useful?</strong></td>
    <td>The bar graph is the most useful because it clearly shows the proportion of each tool’s popularity in different states.</td>
    <td>The bar chart is more useful as it allows for easier comparison across states.</td>
  </tr>
  <tr>
    <td><strong>Is there anything you would change or do differently?</strong></td>
    <td>I would change the map to show multiple tools in each state using gradients or pie charts.</td>
    <td>I would change the map to show proportional usage of tools in each state, and allow the bar chart to be sortable based on different tools.</td>
  </tr>
  <tr>
    <td><strong>Do you think the colors used in the chart are helpful?</strong></td>
    <td>The colors are clear and distinct, but a gradient might work better for showing differences in usage.</td>
    <td>Yes, the colors are helpful, but gradients or shading could better represent proportional usage on the map.</td>
  </tr>
  <tr>
    <td><strong>Would you prefer another type of chart or representation?</strong></td>
    <td>I’d prefer gradients or pie charts on the map to better show multiple tools in each state. The bar graph works well as is.</td>
    <td>A proportional or stacked chart for the map would be better, and the bar chart could benefit from sorting options for easier comparison across tools.</td>
  </tr>
</table>

## Step 5: Build your solution
### Viz 1
<div class='tableauPlaceholder' id='viz1726548166974' style='position: relative'><noscript><a href='#'><img alt='Exploring AI Image Generation Trends Across U.S. StatesThis interactive map features donut charts to represent the search interest distribution for DALL-E, MidJourney, and Stable Diffusion across different U.S. states. Each chart visualizes the proporti ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;YS&#47;YS7CDR5GQ&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;YS7CDR5GQ' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;YS&#47;YS7CDR5GQ&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>             
<script type='text/javascript'>                   
  var divElement = document.getElementById('viz1726548166974');                   
  var vizElement = divElement.getElementsByTagName('object')[0];                  
  vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                 
  var scriptElement = document.createElement('script');                   
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                
  vizElement.parentNode.insertBefore(scriptElement, vizElement);                
</script>
<br>

The donut chart overlay on the map provides geographic context to the AI tool usage data. By displaying the data directly on a map, users can easily identify regional trends and see how each AI tool (MidJourney, Stable Diffusion, DALL-E) is used within specific states. The donut slices visually represent the proportional usage of each tool, making it intuitive to identify which tools are most popular in different regions.

Interaction Features:
- **Hover Over for State Name:** Users can hover over the white center of each donut to reveal the state’s name, ensuring easy identification of each geographic region.
- **Hover Over for Tool Usage:** Users can hover over the colored sections of the donut to see the percentage usage of each AI tool (blue for MidJourney, red for Stable Diffusion, yellow for DALL-E). This feature provides a clear breakdown of tool preferences within each state.
  
### Viz 2
<div class='tableauPlaceholder' id='viz1726548219607' style='position: relative'><noscript><a href='#'><img alt='Exploring AI Image Generation Trends Across U.S. StatesThis visualization compares the search interest for three major AI image generation tools—DALL-E, MidJourney, and Stable Diffusion—across U.S. states. The bar chart displays the proportion of search ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;GZ&#47;GZ787X4TR&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;GZ787X4TR' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;GZ&#47;GZ787X4TR&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>            
<script type='text/javascript'>                   
  var divElement = document.getElementById('viz1726548219607');       
  var vizElement = divElement.getElementsByTagName('object')[0];                  
  vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                 
  var scriptElement = document.createElement('script');                
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                
  vizElement.parentNode.insertBefore(scriptElement, vizElement);            
</script>
<br>

The stacked bar chart provides a clear visual comparison of AI tool usage across different U.S. states. The stacked layout allows users to see the proportion of each tool's usage (Midjourney, Stable Diffusion, DALL-E) in each state, making it easy to compare how these tools are used on a state-by-state basis. The horizontal layout keeps the comparison organized and concise.

Interaction Features:
- **Clicking on Colors:** Users can interact with the chart by selecting individual tool colors on the bar. This feature allows users to filter the chart by the selected tool, instantly reorganizing the chart to highlight the chosen tool. The selected tool will appear first in the bar distribution across all states, making it easier to focus on how the tool performs regionally.
- **X-Axis Percentages:** The X-axis is labeled with percentages, helping users to easily interpret the data proportions, showing the popularity of each tool as a percentage of the total across all states.
  
Video Reference: [#WatchMeViz Generative AI Search Trends in the United States](https://www.youtube.com/watch?v=-w0ynF43yZg&list=PLX-uPHRG0cLb697Ie-ZGSObRLLNhxzJGK&index=11)
<br>
### Class Critique
In the class critique, it was pointed out that the x-axis label was repetitive, particularly with the inclusion of "statewide," which wasn’t necessary. Additionally, the bars in the chart were too wide, making the visualization feel cramped and harder to interpret. The feedback also mentioned that the map visualization wasn’t useful, as it was unclear and didn’t facilitate easy comparison between states, suggesting that the bar chart alone would suffice. Finally, it was recommended that the header could be more engaging to better capture attention, and it was emphasized to consider the intended audience, which includes marketers, AI developers, and data analysts.

## Step 6: Final solution
<div class='tableauPlaceholder' id='viz1726595355062' style='position: relative'><noscript><a href='#'><img alt='AI Image Wars: U.S. States&#39; Search PreferencesThis visualization highlights regional preferences for three major AI image generation tools—DALL-E, MidJourney, and Stable Diffusion—based on search interest across U.S. states. Users can interact by select ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;6J&#47;6JW7Y8H9P&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;6JW7Y8H9P' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;6J&#47;6JW7Y8H9P&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>        
<script type='text/javascript'>                 
  var divElement = document.getElementById('viz1726595355062');                    
  var vizElement = divElement.getElementsByTagName('object')[0];                    
  vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                   
  var scriptElement = document.createElement('script');                  
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                  
  vizElement.parentNode.insertBefore(scriptElement, vizElement);              
</script>
<br>
In this final version, I made several enhancements based on the feedback I received. Firstly, I simplified the x-axis label to "Search Interest Share (%)" to avoid redundancy, making it more concise and aligned with the data. I also reduced the width of the bars, allowing for more breathing space and making the chart easier to read. Additionally, I removed the map visualization as it was considered unclear and difficult to compare, focusing solely on the bar chart for clearer data interpretation.

To make the visualization more engaging, I added a catchier title—"AI Image Wars: U.S. States' Search Preferences"—which immediately grabs attention and sets the tone for the data being presented. This version caters to the intended audience of marketers, AI developers, and data analysts, who will appreciate the straightforward, comparative nature of the chart. Lastly, I refined the interaction instructions, encouraging users to select or deselect tools in the legend or click on a bar to bring the tool of interest to the forefront, ensuring a seamless and interactive experience.
