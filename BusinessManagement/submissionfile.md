<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Abhinav Chowdawaram (ac2526)</td></tr>
<tr><td> <em>Generated: </em> 12/5/2022 8:05:29 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/ac2526" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205609754-41e4fcbd-637f-4bfa-8b55-6edfabfd26b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing index page being displayed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205609932-dc9386fa-ad76-4b3d-b01c-b3cbd4d7945d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing companies table with data in VS code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205609983-ed207ae1-dc3e-43dc-bb94-ac1aa292e51d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing employee table with data in VS code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205612712-b74f6a0c-f6fa-4d26-ad0c-69383c5c1e57.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing tables created for companies and employee<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205610344-4b936d53-a6da-421b-9d0b-a1ea0a6f5b66.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for checking if the file is a .csv file otherwise reject with<br>a flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205611073-19da828a-8a7b-44e8-8819-2ba7bd322397.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot code of reading from the provided stream as a dict, Extracted employee<br>and companies data appended as a dict and a flash message generating how<br>many records were processed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205611629-2707548f-9b16-49b4-9a87-158e2a990f9d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for flash message for generating how many records were processed and flash<br>message for a unloaded or empty list<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205612010-29f505a0-349e-4fc5-b00d-b9dbd8c577f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of proper success message for uploading the data and showing the count<br>of records<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205612197-ae6505d5-e944-4cc2-a53a-8e2e7e4cd41f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the error message when the file is not a .csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205612380-e033e3be-5556-48e3-9309-d1a368129bbb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the error message when the form was submitted without a file attached<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205612489-c05d4598-bac4-448a-b76b-464c675ac398.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot showing in VS code some employee data was uploaded <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205612568-8e9b56f6-9773-4ddb-8b4b-e448b86a595b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot showing in website some employee data was uploaded <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205612633-082ca939-83b8-4cff-b693-9712d52af61b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot showing in VS code some company data was uploaded <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205612596-182f4d2c-755b-4430-a778-5af485e7f16e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot showing in website some company data was uploaded <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205612868-6004029a-4ca8-4ee6-84a5-0646a225cbf9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1,2,3,4,5 - retrieve first_name, last_name, company (id), email and flash error message for<br>first_name, last_name, email is required as company may be empty/none<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205612970-5526eeb7-8c1a-4c85-bca0-10aaaa5dbbec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6,7 - insert query and a except block having a user friendly message<br>flashed and a print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205613341-4b430736-4853-4660-8c79-047e9aa320a2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing filled in valid data prior to submissin<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205613571-bdbceb06-a704-4ab8-89b6-7083aabc1eff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing employee adding success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205613642-7ab1c3cc-5661-43a5-99e2-f47a65cc2c46.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205613700-aa8ea049-e5a7-4380-906a-d895c64fa6af.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205613744-1fbe8e7b-ba3a-42a1-818c-1fda8dde85b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205613841-61cd2ccd-1f2e-439d-b5f2-a11a300ac32d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing the new employee record that was added previously.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205613918-e1444c9d-2379-47d4-bd27-ca380e4b07b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1,2,3,4,5 - SELECT query to to pull employ id, first_name, last_name, email, company_id,<br>company_name via a LEFT JOIN, Checking request args for fn, ln, email, company,<br>column, order, limit, appending like filter for first_name, last_name, email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205613947-eca5f757-2ddf-4a18-a190-7f10c9ce6f9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#6,7,8 - appending equality filter for company_id, appending sorting if column and order<br>are provided and within the allowed columns and order options, append limit (default<br>10) or limit greater than 1 and less than or equal to 100<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205613980-8db4ba59-bc70-4551-960f-fe90a0f8d07b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#9,10 - code for provideing a proper error message if limit isn&#39;t a<br>number or if it&#39;s out of bounds, Except block having a user friendly<br>message flashed and a print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205614059-d980179c-ff08-4a92-ab16-3a5138c15871.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205614128-ac9bce73-6ec5-4549-8d7b-adacb87007b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205614184-7d8f8490-56bc-4c45-8db8-7fb31180681c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205614235-5471e264-6873-415d-a5dd-ea45f7e179e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205614276-7ebbdc4f-49d4-4991-9b05-1c170aff21db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing one asc filter applied - choosing Last_name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205614314-0e3fb6d9-f69f-4b7a-baea-672a04a25f18.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing one desc filter applied - choosing Last_name<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205619888-5c3b0dcc-89b6-40fe-8f7a-607e1cbffe82.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing code for (#1,2,3,4,5) - retrieve id (from request args) first_name, last_name, company<br>(id), email from form, flash proper error message for first_name,last_name,email is require and<br>company may be none. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205619923-0ac3c54f-ace1-45dd-be59-39425412beb2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing code for (#6,7,8,9) - proper update query, except blocks that have a<br>user friendly message, proper select query, employee data for passing to the render<br>template.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205625015-9e6c01fc-2c69-4d16-b5f3-23f479bd4c93.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205625048-db26740f-3a1c-42d1-b3b9-4d2a16111548.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing data after an edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205625076-b621b991-98aa-4a18-b30e-33bca0c3fc9e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the original data from the VS code database of an employee who&#39;s<br>id is 410<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205625115-298831f2-ffeb-4cdb-b7e6-a9b18462bf15.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing the screenshot after editing in which i have edited the person first_name<br>by adding &quot;-editing&quot; word to the existing name.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205626510-0033f4d1-aa87-4663-80cf-f962e12a3aa3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1,2,3,4,5,6,7 - code for retrieve from data for name, address, city, state, country,<br>zip, website, and flash error message for name, address, city, state, country, website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205626547-cb95bd43-8ced-45a2-bcb9-ed0bd415ec64.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#8,9 - code for proper insert query and a except block which have<br>a user friendly message flashed and a print() of exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205629150-6e1d2b76-1c7c-48c3-beb1-04843d8a5518.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot Showing filled in valid data prior to submissin<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205629180-88b39e9a-b20f-46d6-bfec-c505eb141cb6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot Showing success message for adding a new company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205629303-decde775-0d81-4c39-a949-f38427ac47d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot Showing name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205629342-4cf2df8a-9914-43b0-a091-ed48d43628e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot Showing address error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205629395-0d55dc7e-a1f5-499d-ae85-28bb5e46e80f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot Showing city error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205629457-bab5916e-e478-43a6-bfc7-92af0bddeadf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot Showing state error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205629532-aaa82047-6126-4487-b9e7-7274021bf373.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot Showing country error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205630335-84ae51a8-1d63-4a36-b9f6-7cf688952939.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the company that was added previously<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205632012-9fe50562-f3c7-4406-a39b-68a11cd9f45f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1 - screenshot of SELECT query should fetch id, name, address, city, country,<br>state, zip, website, employee count for the company (likely a sub-query is needed)<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205632052-b1dbf198-c100-4fb2-a10d-8407d04eda95.png"/></td></tr>
<tr><td> <em>Caption:</em> <h1 id="23456---screebshot-for-checking-request-args-for-name-country-state-columnorder-limit-appeding-a-like-filter-for-name-and-equality-filter-for-stateand-country-and-sorting-if-column-and-order-are-provided-and-within-theallows-columsn-and-allowed-order-ascdesc">2,3,4,5,6 - screebshot for Checking request args for name, country, state, column,<br>order, limit, appeding a like filter for name and equality filter for state<br>and country and sorting if column and order are provided and within the<br>allows columsn and allowed order asc,desc<br></h1>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205632073-d18f8966-0253-4770-989b-33f0207f25a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#7,8,9 - append limit (default 10) or limit greater than 1 and less<br>than or equal to 100, providing a proper message if limit isn&#39;t a<br>number or if it&#39;s out of bounds, and Except block that have a<br>user friendly message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205634854-c5c951d2-ed1e-48c6-b2e9-8cc1e225c9a0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205634934-23c2b13c-031f-4c23-b1bc-c745719e00bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205634965-5436d3d8-8d5b-430f-a16f-bf0cbf8a88f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205634997-382e9fc9-c6d5-44bf-ba36-e03714286560.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing one asc filter applied with a city column<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205635030-4eb1f3bb-655e-445b-a30a-52ef28d28c42.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing one desc filter applied with a city column<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205636491-e65eb158-a644-43fc-81bb-27a9d421506c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#1,2,3,4 Code that have retrieved from the given arguments, and a flash error<br>message for name, address, city.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205636695-77fb2843-9960-443c-b7ba-54979ee8967d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#5,6 - Screenshot showing code for flash error message for state and country<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205636729-7fc46f7b-9861-4452-845f-1c61abea547e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>#7,8,9 - Screenshot showing code for proper update query,except blocks that have a<br>user friendly flash message  and a proper select query and the company<br>data have passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205639339-95431fe5-a7bd-4c76-a8c5-2ecbdf588a0f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing east coast company before editing in the website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205639362-15c41e91-1ad6-4401-b0b0-955bb1fd056a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing east coast company after editing the name by adding the word<br>&quot;-edited&quot; in the website<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205639407-cb5d8cf7-9ea3-4212-890e-5df022721149.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing east coast company before editing in the VS code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205639430-e4ba8706-544f-44b3-aa44-ab8db8a3975f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing east coast company after editing the name by adding the word<br>&quot;-edited&quot; in the VS code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205640254-cc61d3ea-c613-4239-99f9-da5bc5cef320.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the code which contains the lines Delete employee by id, Redirect<br>to employee search, All request args (minus id) are passed to the redirect<br>route, Success message will be flashed when the process worked<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205641520-835dbcd3-5e08-4a77-b071-31714746dd8d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing of the search results for marti before deleting the employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205641547-6f23c641-5a8c-4247-a3a4-3746464d3032.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing of search results for marti after deleting a employee with a<br>success message for employee deletion marti<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205640290-51955657-2005-44e2-a36d-7f8f4fb7ef00.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows the code which contains the lines Delete company by id, Redirect<br>to company search, All request args (minus id) are passed to the redirect<br>route, Success message will be flashed when the process worked<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205642998-6b4cd523-cf8a-433d-861c-f231bba27517.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing results for xyz before deleting.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205643032-fc784d03-ed39-400e-aab4-4697b175fd16.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing results for xyz after deleting with 0 results and a success<br>message for deletion<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113549290/205635425-7bef49e7-5929-4af5-b84b-b947bd5ab960.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing all the test cases passed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>while working on this project I have learned a lot about interesting topics<br>like web development, test cases, and handling databases through python.<br>Initially, I was struggling<br>with the python interpreter path which was not able to read the packages<br>that were installed in the virtual environment, and then I realized and changed<br>the path to python from venv then&nbsp; all my warnings and errors were<br>gone.<br><br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/ac2526" target="_blank">Grading</a></td></tr></table>