# GitHub Pages Deployment Instructions for `simcalc/pv_sim`

This guide will walk you through the steps to deploy your project using GitHub Pages.

## Prerequisites
- Ensure you have a GitHub account and have access to the `simcalc/pv_sim` repository.
- Familiarity with Git and GitHub is helpful, but not required.

## Steps for Deployment

### 1. Prepare Your Project
- Make sure your project is in the main directory of your repository. This means your HTML, CSS, and JavaScript files should be readily accessible.

### 2. Create a `gh-pages` Branch
- Go to your repository on GitHub.
- Click on the **branches** dropdown menu.
- Type `gh-pages` in the branch name field and press Enter.
- Switch to the new `gh-pages` branch.

### 3. Add Your Files
- Ensure the necessary files (like `index.html`) are in the `gh-pages` branch. You can do this by either manual file upload via GitHub or by using command line git commands:
    ```bash
    git checkout gh-pages
    git merge main
    git push origin gh-pages
    ```

### 4. Enable GitHub Pages
- Go to your repository's Settings.
- Scroll down to the **Pages** section.
- Select the `gh-pages` branch as the source. Click **Save**.

### 5. Access Your Deployed Site
- After a couple of minutes, your GitHub Pages site will be available at `https://<username>.github.io/<repository-name>/`.
- In your case, it would be `https://simcalc.github.io/pv_sim/`.

### 6. Update Your Site (if necessary)
- To make updates to your site, add your changes to the `main` branch and merge to `gh-pages` as shown above.

### Troubleshooting
- If you encounter any issues, check the **Pages** section in your repository settings for error messages.
- Ensure your `index.html` file exists and is correctly formatted.

## Conclusion
You have successfully deployed your project using GitHub Pages! For more information, visit the [GitHub Pages documentation](https://docs.github.com/pages).