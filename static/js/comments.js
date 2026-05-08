const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_text");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("commentSubmitButton");

/**initialises edit functionality for the provided edit button.
 * 
 * for each button in the 'editButtons' collection:
 * Retrieves the associated comment's ID upon click
 * Fetches the content of the corresponding comment.
 * Populates the 'commentText' input/textarea with the comment's content for editing
 * updats the submit buttons's text to "Update".
 * Sets the form's action attribute to the 'edit_comment/commentID' endpoint
 */

for (let button of editButtons){
    button.addEventListener('click', (e) =>{
        let commentId = e.currentTarget.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`)
    })
}
    