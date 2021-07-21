document.getElementById('user-name').focus();

const loginButton = document.getElementById('login-button');
loginButton.onclick = function () {
  const input = getIdAndPass();
  if (!input.valid) return;
  if (checkAuth(input.id, input.pass)) {
    const idAndPass = { [input.id]: input.pass };
    const sendData = JSON.stringify(idAndPass);
    const url = 'https://i6uxckr3u8.execute-api.ap-northeast-1.amazonaws.com/dev/login';
    console.log(sendData);
    // doPost(url, sendData);
    const hoge = postData(url, sendData);
    console.log(hoge);
    alert('login success');
    // window.location.href = '../page/todo.html';
    window.location.href = 'http://localhost:8001/list';
    
  } else {
    alert('faild login');
  }
};

const newAccountButton = document.getElementById('new-account-button');
newAccountButton.onclick = function () {
  const input = getIdAndPass();
  alert('新しいアカウントを作ります');
};

function getIdAndPass() {
  const id = document.getElementById('user-name');
  const pass = document.getElementById('password');
  const valid = true; // check valid id or password
  return { valid: valid, id: id.value, pass: pass.value };
}

function checkAuth(id, pass) {
  // server API?
  return id.toString().length >= 4 && pass.toString().length >= 8; // test
}

function doPost(url, data) {
  console.log(url);
  let xhr = new XMLHttpRequest();
  xhr.onload = () => {
    console.log(xhr.status);
    console.log('success!');
  };
  xhr.onerror = () => {
    console.log(xhr.status);
    console.log('error!');
  };
  xhr.open('POST', url, true);
  console.log(xhr.status);
  console.log(xhr.response);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(data);
  console.log(xhr.status);
  console.log(data);
}

function postData(url = '', data = {}) {
  // 既定のオプションには * が付いています
  const response = fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data) // 本文のデータ型は "Content-Type" ヘッダーと一致する必要があります
  });
  console.log(response.ok);
  console.log('hoge');
  // return response.json(); // レスポンスの JSON を解析
}

function next_text(idx) {
  if (window.event.keyCode == 13) {        // 13は0x0d(CRキー)
    // 次のテキストボックスへ飛ばす処理をここにかく

    if (idx == 2) {
      loginButton.onclick();
    }

    document.loginForm.text1[idx].focus();

    return false;
  }
  return true;
}