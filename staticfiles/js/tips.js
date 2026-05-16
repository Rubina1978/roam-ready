
// const tipContent = document.getElementById("tip");
// const tipForm = document.getElementById("tipForm");
// const submitButton = document.getElementById("tipSubmitButton");

const tipEditButtons = document.getElementsByClassName("btn-edit-tip");
const tipDeleteButtons = document.getElementsByClassName("btn-delete-tip");
const tipType = document.getElementById("id_tip_type");
const tipContent = document.getElementById("id_content");
const tipForm = document.getElementById("tipForm");
const tipSubmitButton = document.getElementById("tipSubmitButton");

/**initialises edit functionality for the provided edit button.
 * 
 * for each button in the 'editButtons' collection:
 * Retrieves the associated comment's ID upon click
 * Fetches the content of the corresponding comment.
 * Populates the 'commentText' input/textarea with the comment's content for editing
 * updats the submit buttons's text to "Update".
 * Sets the form's action attribute to the 'edit_comment/commentID' endpoint
 */


for (let button of tipEditButtons){
  button.addEventListener('click', (e) =>{
    let tipId = e.currentTarget.getAttribute("data-tip-id");
    let tipTypeValue = document.getElementById(`tiptype${tipId}`).innerText;
    let tipText = document.getElementById(`tip${tipId}`).innerText;
    tipType.value = tipTypeValue;
    tipContent.value = tipText;
    tipSubmitButton.innerText = "Update";
    tipForm.setAttribute("action", `edit_tip/${tipId}`)
});
}

// deleting of tips

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of tipDeleteButtons) {
  button.addEventListener("click", (e) => {
    let tipId = e.currentTarget.getAttribute("data-tip-id");
    let destinationId = e.currentTarget.getAttribute("data-destination-id");
    deleteConfirm.href = `/${destinationId}/delete_tip/${tipId}/`;
    deleteModal.show();
  });
}