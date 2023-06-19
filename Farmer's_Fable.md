# Farmer's Problem

This problem originated from the following website, https://www.farmersfable.org/?authuser=0

As a scientist, I was skeptical about the moral of the story, where cooperating will always be beneficial for the individual's outcome and would always be gaining more in a geometric level. Without reading the science behind, I believed I was right and it should solely be a result from the imbalanced gain-loss factor being used in the example.</br>

See, the gain factor used in the example was 1.5, whereas loss factor was 0.7. As $1.5^{-1}=0.66$, so obviously $1.5*0.7>1$ must be true and in fact, $0.7*1.5=1.05$ and $1.05^{100}=131.501$ was the first intuition to the explaination to the problem. But no, science need prove and this explanation would explain why the cooperative outcome is that much higher(or we can still explain it as it lower the risk of loss by spliting the investment in half every time).<br>

But still, what could be more convincing than doing a full simulation on all possible gain-loss parameters and see if it is still beneficial to the system, if in any setting, the cooperative outcome outloss the individual ones would an evidence to prove this idea is simply wrong.<br>

So I first built a single gain-loss factor farm simulation with 100 rounds of harvest as similar to the story's setting

You can see the raw data or even try out the simulation yourself, I couldn't figure out how to make python work in a markdown page but it is user inputable program as I finialised my build, anyway the truth is, I was wrong!!

This is the result of the simulation even after 1000 rounds of harvest,<br>
![simulation_result](Farmer's_Fable\qualitative_result_on_deepscan_simulations_grid.png)
All the green dots mean those settings are benefited from cooperation, where 2 times the cooperation outcome is larger than the sum of individual outcomes. Only when gain-loss factor are both 1,1, we would have a unity where the cooperation is equal to the individual outcome so no benefits!(which makes sense as 1 times 1 is one ok?)