const xhr = new XMLHttpRequest();

xhr.open('GET', 'cal.json', true);

xhr.onload = function () {
  if (this.status === 200) {
    const calData = JSON.parse(this.responseText);

    console.log(calData.date);
  }
};
