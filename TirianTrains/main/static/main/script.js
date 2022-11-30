const addTripButton = document.getElementById('add-trip');
const trip1 = document.getElementById('trip-1')

addTripButtonListener = (e) =>{
    const selectContainer = e.target.parentNode.parentNode; 
    const nameId = `trip-${selectContainer.children.length}`;
    const buttonsDiv = selectContainer.lastElementChild 
    const tripSelector = trip1.cloneNode(true)
    tripSelector.setAttribute('name', nameId)
    tripSelector.setAttribute('id', nameId)
    tripSelector.required = false;
    selectContainer.insertBefore(tripSelector, buttonsDiv)
    
}

addTripButton.addEventListener("click", addTripButtonListener)