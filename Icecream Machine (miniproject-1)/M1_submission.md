<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - IceCream</td></tr>
<tr><td> <em>Student: </em> Abhinav Chowdawaram (ac2526)</td></tr>
<tr><td> <em>Generated: </em> 10/25/2022 10:17:52 PM</td></tr>
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
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197917978-5bca790c-af6c-416f-a0c8-265349c15fd5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the OutOfStockException is handled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197918005-b43049d3-cb88-44dc-9198-892362beecc4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the NeedsCleaningException is handled <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197918077-84fb43b3-4dd3-4c5f-be1d-db1fb15a8542.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the InvalidChoiceExceptions are handled for container<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197918106-3406e1e4-63e4-4961-947e-61ef986164a5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the InvalidChoiceExceptions are handled for toppings<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197918124-e61490c9-b0b8-43a4-b268-af1be4086bdb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the InvalidChoiceExceptions are handled for flavors<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197918178-b3eede44-dde4-45c6-ac2a-b5647b5d3c68.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the ExceededRemainingChoicesExceptions are handled for flavors<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197918200-bd2d350b-d050-44ae-8773-04453dc53f6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the ExceededRemainingChoicesExceptions are handled for toppings<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197918226-0d8703c9-e981-4520-bc55-70b63663613f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows how the InvalidPaymentException is handled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p>When a user wants to add an item but there is no quantity<br>for that item, OutOfStockException is raised.<br>NeedsCleaningException is called when the user requests another<br>ice cream after &quot;USES UNTIL CLEANING&quot; the allotted number of ice creams have<br>been supplied.<div>InvalidChoiceException is generated if the user selects a non-choice option that is<br>invalid.</div><div>All ice creams have a maximum number of scoops and toppings that can<br>be added before ExceededRemainingChoicesException is generated.</div><div>InvalidPaymentException is raised if the user enters a<br>value other than the precise value.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197918378-3e0dc179-ac40-4fff-95da-0931295b8df5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot contains the tests of container selection, adding flavors and toppings only<br>if there are in stock (Test - 1, 2, 3)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197918395-4d43352a-0573-4a12-826a-d918ddb74ea4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot contains the tests of maximum scoops and toppings ( Test -<br>4, 5)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197918412-6a024ae7-6e08-4e63-9641-1df73f9d94f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot contains the test case which test the cost based on the<br>choices(Test - 6)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197918430-7760875a-898b-4ef5-8601-6a56bab47ad1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot contains the test case which test the Total Sales (sum of<br>costs).(Test - 7)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197918449-53238875-756e-4252-a7b8-c22a2ee6b82c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot contains the test case which test the Total icecreams that properly<br>increment for each purchase(Test - 8)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197918477-e33ed09e-8328-4b4c-97f7-3d44e3254e95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot showing all the Test 1-8 passing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div>Test 1: test_first_selection - checks if the first stage is the container</div><div>stage</div><div>Test 2:<br>test_flavour_in_stock - changing the ice cream machine item quantity to</div><div>1 and testing to<br>see if the item can be added twice, OutOfStockException</div><div>should be raised</div><div><br></div><div>Test 3: test_toppings_in_stock<br>- changing the ice cream machine item quantity</div><div>to 1 and testing to see<br>if the item can be added twice,</div><div>OutOfStockException should be raised</div><div>Test 4: test_max_scoops -<br>used a loop to add</div><div>a scoop max_scoops(3) times and if another scoop is<br>added, then ExceededRemainingChoicesException should</div><div>be raised</div><div>Test 5: test_max_toppings - used a loop to add<br>a scoop max_toppings(3) times</div><div>and if another topping is added, then ExceededRemainingChoicesException should be<br>raised</div><div>Test 6: test_total_cost - added a</div><div>container, some scoops, and some toppings and calculated<br>the sum, and asserted the</div><div>sum to be equal to the cost calculated from<br>the method</div><div>Test 7: test_total_sales - added 2 ice creams, made valid payments for<br>both, and asserted the total</div><div>sales to be equal to the sum of the<br>2 ice creams' cost</div><div>Test</div><div>8: test_total_icecreams - added 3 ice creams, made valid payments<br>for both and asserted</div><div>the total ice creams to be equal to 3, used<br>the pytest fixture</div><div>second_order which has 2 ice creams delivered, and asserted the total<br>ice creams</div><div>for the second order to be 2</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AbhinavC12/IS601-005-31597122/pull/30">https://github.com/AbhinavC12/IS601-005-31597122/pull/30</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>No major issues.<br>I was always curious about how these testing methods while attempting<br>competitive examinations and because of this assignment I have learned about it.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197918552-32d2f72a-bc05-4164-8d2e-ab8f97a94f31.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot contains 2 different ice cream selections, which asks for the containers,<br>flavors, toppings and return the total cost for the ice cream<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/197918614-ce365b4d-e9fb-4dd0-847c-0e3d75c5b581.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot contains 3rd type of ice cream selections, which asks for the<br>containers, flavors, toppings and return the total cost for the ice cream<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-1-icecream/grade/ac2526" target="_blank">Grading</a></td></tr></table>
