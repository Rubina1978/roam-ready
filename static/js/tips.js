
// const tipContent = document.getElementById("tip");
// const tipForm = document.getElementById("tipForm");
// const submitButton = document.getElementById("tipSubmitButton");

const tipEditButtons = document.getElementsByClassName("btn-edit");
// const tipType = document.getElementById("id_tip_type");
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
        let tipId = e.currentTarget.getAttribute("tip_id");
        let destinationId = e.currentTarget.getAttribute("destination_id");
        let tipText = document.getElementById(`tip${tipId}`).innerText;
        tipContent.value = tipText;
        tipSubmitButton.innerText = "Update";
        tipForm.setAttribute("action", `edit_tip/${tipId}`)
});
}
// const tipButtons = document.getElementsByClassName("btn-edit");
// const tipContent = document.getElementById("id_content");
// const tipType = document.getElementById("id_tip_type");
// const tipForm = document.getElementById("tipForm");
// const tipSubmit = document.getElementById("tipSubmitButton");

// for (let btn of tipButtons) {
// btn.addEventListener('click', function () {
// const tipId = this.getAttribute('tip_id');
// tipContent.value = document.getElementById('tip' + tipId).innerText;
// tipType.value = document.getElementById('tiptype' + tipId).innerText;
// tipSubmit.innerText = 'Update';
// tipForm.action = /${this.getAttribute('destination_id')}/edit_tip/${tipId};
// });
// }