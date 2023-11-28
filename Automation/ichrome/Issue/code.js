document.querySelector("div[class~=CodeMirror]").focus()

navigator.clipboard
  .readText()
  .then(
    (clipText) => (console.log(clipText))
  );


  document.dispatchEvent(
    new KeyboardEvent("keydown", {
        key: "v",
        ctrlKey: true,
        bubbles: true,
        metaKey: true   
    })
);

https://erikmartinjordan.com/simulate-multiple-keypress-javascript