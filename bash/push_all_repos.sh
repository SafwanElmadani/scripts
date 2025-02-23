#!/bin/bash

# Check if a file containing repo paths is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <repo_list_file> [commit message]"
    exit 1
fi

# File containing repo paths
REPO_LIST_FILE="$1"

# Use the provided commit message or default to a timestamp-based message
COMMIT_MESSAGE="${2:-Auto-commit: $(date)}"

# Check if the file exists
if [ ! -f "$REPO_LIST_FILE" ]; then
    echo "Error: File '$REPO_LIST_FILE' not found!"
    exit 1
fi

# Function to process each Git repository
process_repo() {
    local repo_path="$1"
    
    # Check if the directory exists and is a Git repository
    if [ ! -d "$repo_path/.git" ]; then
        echo "Skipping: $repo_path (Not a Git repository)"
        return
    fi
    
    echo "Processing: $repo_path"
    cd "$repo_path" || return

    # Pull the latest changes from the remote repository
    echo "Pulling latest changes in $repo_path"
    git pull

    # Check for uncommitted changes
    if git status --porcelain | grep -q .; then
        git add .
        git commit -m "$COMMIT_MESSAGE"
        git push
        echo "Pushed changes in $repo_path"
    else
        echo "No changes to push in $repo_path"
    fi
}

# Read the file and process each repository
while IFS= read -r repo_path; do
    # Ignore empty lines and comments
    [[ -z "$repo_path" || "$repo_path" == \#* ]] && continue

    process_repo "$repo_path"
done < "$REPO_LIST_FILE"

echo "All repositories processed."
