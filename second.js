function predict() {
  const input = document.getElementById('input').value;
  fetch('file:///C:/Users/Admin/Desktop/Dental%20Project/site/mainproject-main/index.html', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({input: input})
  })
  .then(response => response.json())
  .then(data => {
    const output = document.getElementById('output');
    output.innerHTML = 'Predicted result: ' + data.result;
  })
  .catch(error => console.error(error));
}