The Constrain-O-Matic lets you create multiple constraints at once. Let's use the Constrain-O-Matic in context to see how it works.

After installing the Python script in the appropriate folder, I set up a button to run the code to import and create the UI. The necessary code can be found in the README or "How To Install" files.

Clicking the button brings up the tool UI. THere are input fields for your filter strings, checkboxes to enable the constraints you wish to use, and two buttons to execute the code.

For this demo, let's start with "One By One" mode. "One By One" will connect pairs of objects to each other. I want to connect cubes A, B, and C to spheres 1, 2, and 3, respectively. Above, you can see that the spheres share a hierarchy, but are not yet connected to the cubes in any way. 

I need to tell the tool which objects to attach to which. To do so, I'll need a filter string to help the program sort out what's going to be a parent and what's going to be a child. The parent and child strings will automatically sort through your selected objects and place the parents in one list and the children in another list. Because all the spheres are named similarly, we'll use "sphere" for the parent string. I'll do the same for the child string, putting "cube" in the input field.

Now I can select all the cubes and spheres at once. Your selection order doesn't impact the results: the script alphabetizes your selection, so in this case, A connects to 1, B to 2, and C to 3.

I'll activate the Point constraint checkbox and click "One By One". There are now Point constraints on each cube, connecting their translations to the corresponding spheres.

Next, let's try "One For All" mode. "One For All" connects a single parent to as many children as you want it to. In this example, I want the rotation of all three cubes to be constrained to sphere 2. So I will select sphere 2 and the cubes, change the activated constraint from Point to Orient, and click "One For All". Now you can see that new constraints have been added. The cubes now rotate according to the rotation on sphere 2.

Below is a timelapse example of me using the Constrain-O-Matic to connect all parts of a mechanical hand rig in under three minutes.
