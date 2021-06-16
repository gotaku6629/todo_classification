'use strict';


const table1 = document.getElementById('table1');
const table2 = document.getElementById('table2');
const table3 = document.getElementById('table3');
const table4 = document.getElementById('table4');
const table5 = document.getElementById('table5');
const todo = document.getElementById('todo');
const submit = document.getElementById('submit');

const addItem = (item) => {
    const tr = document.createElement('tr');
    for (const prop in item) {
      const td = document.createElement('td');
      
      if (prop == 'done') {
        
      } else {
        td.textContent = item[prop];
      }
      tr.append(td);
      
    }
    if (item.todo == "a") {
        table1.append(tr);
    }else if (item.todo == "b") {
        table2.append(tr);
    }else if (item.todo == "c") {
        table3.append(tr);
    }else if (item.todo == "d") {
        table4.append(tr);
    }else if (item.todo == "e") {
        table5.append(tr);
    }
};



submit.addEventListener('click', () => {
  const item = {};

  if (todo.value != '') {
    item.todo = todo.value;
  } 

  todo.value = '';

  addItem(item);


});





