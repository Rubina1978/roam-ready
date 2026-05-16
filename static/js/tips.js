/* jshint esversion: 11 */
/* global deleteConfirm, deleteModal */

const tipEditButtons = document.getElementsByClassName("btn-edit-tip");
const tipDeleteButtons = document.getElementsByClassName("btn-delete-tip");
const tipType = document.getElementById("id_tip_type");
const tipContent = document.getElementById("id_content");
const tipForm = document.getElementById("tipForm");
const tipSubmitButton = document.getElementById("tipSubmitButton");


for (let button of tipEditButtons){
  button.addEventListener('click', (e) =>{
    let tipId = e.currentTarget.getAttribute("data-tip-id");
    let tipTypeValue = document.getElementById(`tiptype${tipId}`).innerText;
    let tipText = document.getElementById(`tip${tipId}`).innerText;
    tipType.value = tipTypeValue;
    tipContent.value = tipText;
    tipSubmitButton.innerText = "Update";
    tipForm.setAttribute("action", `edit_tip/${tipId}`);
});
}


for (let button of tipDeleteButtons) {
  button.addEventListener("click", (e) => {
    let tipId = e.currentTarget.getAttribute("data-tip-id");
    let destinationId = e.currentTarget.getAttribute("data-destination-id");
    deleteConfirm.href = 
        `/${destinationId}/delete_tip/${tipId}/`;

    deleteModal.show();
  });
}