$(function(){
    const modal = new bootstrap.Modal(document.getElementById('modal'))



    htmx.on('htmx:afterSwap', (e) => {
        if (e.detail.target.id === "dialog")
        modal.show()
    })
    

})()