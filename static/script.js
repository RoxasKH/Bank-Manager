const HOST_APP_URL = 'http://localhost:5000';

function showMenu() {
  var x = $('#myTopnav');
  if (x.attr('class') === 'topnav') {
    x.addClass(' responsive');
  } else {
    x.removeClass(' responsive');
  }
}

$(document).on('submit', '#getdata-form', function(e) {
  e.preventDefault();
  $('#account_data').html('');
  $('.lds-ring').css('display', 'inline-block');
  $('#account_data').removeClass('error');

  $.ajax({
    type:'GET',
    url:(HOST_APP_URL + '/api/account/' + $('#userid').val()),
    success:function(response)
    {
      $('.lds-ring').css('display', 'none');

      console.log(response.status);

      function getTransactions() {

        var transactions = '';

        if(response[0].transactions.length == 0)
          return `<div id="transaction_table">
                    <table>
                      <tbody>
                        <tr>
                          <td>This account has no transactions.</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>`;

        for (var i = 0; i < response[0].transactions.length; i++) {
          if(response[0].transactions[i].receiver == null)
            receiver = '---';
          else
            receiver = response[0].transactions[i].receiver;

          transactions += `
                <tr>
                  <td>` + response[0].transactions[i].id + `</td>
                  <td>` + receiver + `</td>
                  <td>` + response[0].transactions[i].data + `</td>
                </tr>
              `;
        }

        var transaction_table = `<div id="transaction_table">
            <table>
              <tbody>
                <tr>
                  <th scope="column">Id:</th>
                  <th scope="column">Receiver:</th>
                  <th scope="column">Date:</th>
                </tr> ` 
                + transactions + `
              </tbody>
            </table>
          </div>`

        return transaction_table;

      }

      var data = `
        <div id="account_table">
          <table class="table">
            <tbody>
            <tr>
              <th scope="row">Name:</th>
              <td>` + response[0].name + `</td>
            </tr>
            <tr>
              <th scope="row">Surname:</th>
              <td>` + response[0].surname + `</td>
            </tr>
            <tr>
              <th scope="row">Balance:</th>
              <td>` + response[0].balance + `</td>
            </tr>
            <tr>
              <th scope="row">Transactions:</th>
            </tr>

          </table>

          ` + getTransactions() + `

        </div>

        `;

      $('#account_data').html(data);
    },

    error: function(xhr, statusText, err)
    {
      $('.lds-ring').css('display', 'none');

      $('#account_data').addClass('error');
      $('#description_table').css('opacity', '1');

      $('#account_data').html(
        `Status: &#10006; Error <br><br> <hr>
        <pre>Error Type: ` + xhr.status + ` - ` + err + `</pre>
        <pre>Description: ` + JSON.parse(xhr.responseText).error + `</pre>`);
    }

  })
});


$(document).on('submit', '#transfer-form', function(e) {
  e.preventDefault();

  $('#description_table').css('opacity', '0');

  $('#status').html('');
  $('#description_table').html('');

  $('.lds-ring').css('display', 'inline-block');
  $('#status').removeClass('success error');

  $.ajax({
    type:'POST',
    contentType: "application/json",
    url:HOST_APP_URL + '/api/transfer',
    data:JSON.stringify({
      from:$('#senderid').val(),
      to:$('#receiverid').val(),
      amount:$('#amount').val()
    }),
    success:function(response)
    {
      $('.lds-ring').css('display', 'none');

      var description = `

      <table>
        <tbody>
        <tr>
          <th scope="row">Updated sender amount:</th>
          <td>` + response['' + $('#senderid').val()] + `</td>
        </tr>
        <tr>
          <th scope="row">Updated receiver amount:</th>
          <td>` + response['' + $('#receiverid').val()] + `</td>
        </tr>
        <tr>
          <th scope="row">Transaction ID:</th>
          <td>` + response.trans_id + `</td>
        </tr>
      </table>

      `;
      
      $('#status').addClass('success');
      $('#description_table').css('opacity', '1');
      $('#status').html('Status: &#x2714; Done <br> Amount transferred successfully. <br><br> <hr>');

      $('#description_table').html('<i>Transaction Data:</i> <br><br>' + description);

    },

    error: function(xhr, statusText, err)
    {
      $('.lds-ring').css('display', 'none');

      $('#status').addClass('error');
      $('#description_table').css('opacity', '1');
      $('#status').html('Status: &#10006; Error <br><br> <hr>');

      $('#description_table').html(
        `<pre>Error Type: ` + xhr.status + ` - ` + err + `</pre>
        <pre>Description: ` + JSON.parse(xhr.responseText).error + `</pre>`);
    }

  })
});