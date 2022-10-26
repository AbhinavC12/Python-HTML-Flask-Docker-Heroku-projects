<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - IceCream</td></tr>
<tr><td> <em>Student: </em> Abhinav Chowdawaram (ac2526)</td></tr>
<tr><td> <em>Generated: </em> 10/25/2022 10:41:50 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-1-icecream/grade/ac2526" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216">https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder IcecreamMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197917203-b3c842c6-e1e0-4d5e-ab94-fa371399e59a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the completed lines of calculate_cost() method<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>I determined the price by formatting an iterator that adds up the costs<br>of each item in the list to two decimal places.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921509-966b8adf-7e55-4021-8b1e-3a5a041f9ce7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the OutOfStockException is handled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921549-e0341a3b-7b39-48dc-b105-0ec08f31839b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the NeedsCleaningException is handled <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921577-160aa530-36d5-497c-92fc-7a3a0601e10a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the InvalidChoiceExceptions are handled for container<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921593-5abb4119-c6da-41e2-9419-98254dbef169.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the InvalidChoiceExceptions are handled for toppings<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921641-f741e063-8329-443a-b7f8-49bf86a6c963.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the InvalidChoiceExceptions are handled for flavors<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921699-28bab0fd-61ae-42ea-87bb-b41d676ca6d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the ExceededRemainingChoicesExceptions are handled for flavors<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921727-bdf65f89-798f-49f1-9610-2891b2de344f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the ExceededRemainingChoicesExceptions are handled for toppings<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921743-e9989c95-1228-4474-bd1c-e42b248ef7e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the InvalidPaymentException is handled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p>When a user wants to add an item but there is no quantity<br>for that item, OutOfStockException is raised.<br>NeedsCleaningException is called when the user requests another<br>ice cream after &quot;USES UNTIL CLEANING&quot; the allotted number of ice creams have<br>been supplied.<div>InvalidChoiceException is generated if the user selects a non-choice option that is<br>invalid.</div><div>All ice creams have a maximum number of scoops and toppings that can<br>be added before ExceededRemainingChoicesException is generated.</div><div>InvalidPaymentException is raised if the user enters a<br>value other than the precise value.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921305-43b1fadc-1e5d-474d-af26-354f83700813.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot contains the tests of container selection, adding flavors and toppings only<br>if there are in stock (Test - 1, 2, 3)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921321-ff8f26e4-70fc-4a6c-94ba-17eec5ffb69e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot contains the tests of maximum scoops and toppings ( Test -<br>4, 5)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921333-a2f06e40-497d-46fe-b3d2-f4ba82833ab0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot contains the test case which test the cost based on the<br>choices(Test - 6)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921363-5f7f2b81-8d6e-429e-b734-57787c17e898.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot contains the test case which test the Total Sales (sum of<br>costs).(Test - 7)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921379-d82fe90f-698b-4b9e-a92d-bbe5749a86eb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot contains the test case which test the Total icecreams that properly<br>increment for each purchase(Test - 8)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921405-ecbb4395-59b5-415b-9f67-bb37d0ba4600.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot showing all the Test 1-8 passing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div>Test 1: test_first_selection - checks if the first stage is the container</div><div>stage</div><div>Test 2:<br>test_flavour_in_stock - changing the ice cream machine item quantity to</div><div>1 and testing to<br>see if the item can be added twice, OutOfStockException</div><div>should be raised</div><div><br></div><div>Test 3: test_toppings_in_stock<br>- changing the ice cream machine item quantity</div><div>to 1 and testing to see<br>if the item can be added twice,</div><div>OutOfStockException should be raised</div><div>Test 4: test_max_scoops -<br>used a loop to add</div><div>a scoop max_scoops(3) times and if another scoop is<br>added, then ExceededRemainingChoicesException should</div><div>be raised</div><div>Test 5: test_max_toppings - used a loop to add<br>a scoop max_toppings(3) times</div><div>and if another topping is added, then ExceededRemainingChoicesException should be<br>raised</div><div>Test 6: test_total_cost - added a</div><div>container, some scoops, and some toppings and calculated<br>the sum, and asserted the</div><div>sum to be equal to the cost calculated from<br>the method</div><div>Test 7: test_total_sales - added 2 ice creams, made valid payments for<br>both, and asserted the total</div><div>sales to be equal to the sum of the<br>2 ice creams' cost</div><div>Test</div><div>8: test_total_icecreams - added 3 ice creams, made valid payments<br>for both and asserted</div><div>the total ice creams to be equal to 3, used<br>the pytest fixture</div><div>second_order which has 2 ice creams delivered, and asserted the total<br>ice creams</div><div>for the second order to be 2</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AbhinavC12/IS601-005-31597122/pull/31">https://github.com/AbhinavC12/IS601-005-31597122/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>No major issues.<br>I was always curious about how these testing methods while attempting<br>competitive examinations and because of this assignment I have learned about it.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921253-e649629d-c23a-4540-9105-092e6cd15368.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot contains 2 different ice cream selections, which asks for the containers,<br>flavors, toppings and return the total cost for the ice cream<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197921267-87fdd91a-2390-4c0a-b213-1ad5eb45a89c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot contains 3rd type of ice cream selections, which asks for the<br>containers, flavors, toppings and return the total cost for the ice cream<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-1-icecream/grade/ac2526" target="_blank">Grading</a></td></tr></table>
