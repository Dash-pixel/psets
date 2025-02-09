document.addEventListener('DOMContentLoaded', function() {
  // Use buttons to toggle between views
  
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', () => compose_email ('', '', ''));

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email(recip, sub, bod) {
  // any of this works?
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  const form = document.querySelector('#compose-form');
  const recipients = document.querySelector('#compose-recipients');
  const subject = document.querySelector('#compose-subject');
  const body = document.querySelector('#compose-body');
  recipients.value = recip;
  subject.value = sub;
  body.value = bod;

  
  form.addEventListener("submit", (event) => {
      // change to json object
      // i actually want to select all elements with class form control
      event.preventDefault();
      fetch("/emails", {
        method: "POST",
        body: JSON.stringify({
          recipients: recipients.value,
          subject: subject.value,
          body: body.value
        })
      })
        .then(response => response.json())
        .then(result => {
          // Print result
          console.log(result);
          load_mailbox('inbox');
        });
    })
  
}

function view_email (email_id) {
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  email_box = document.querySelector('#email-view');
  email_box.style.display = 'block';
  email_box.innerHTML = '';

  fetch(`emails/${ email_id }`)
  .then(response => response.json())
  .then((email) => {
      const container = document.createElement('div');
      container.style.padding = '20px';
      container.style.background = '#f4f4f4';
      container.style.border = '1px solid #ddd';
      container.style.borderRadius = '8px';
      container.style.fontFamily = 'Arial, sans-serif';
      container.style.maxWidth = '400px';
      container.style.margin = '20px';
      
      function createParagraphElement(content) {
          const element = document.createElement('p');
          element.textContent = content;
          element.style.margin = '10px 0';
          return element;
      }
      const button = document.createElement('button');
      button.className = 'btn btn-primary';  // Bootstrap button class
      button.textContent = 'Reply';
      const re_subject = (anythin) => (anythin.subject.startsWith("Re: ")) ? anythin.subject.substring(4) : anythin.subject;
      button.addEventListener('click', () => compose_email(
        email.sender, 
        'Re: ' + re_subject(email), 
        'On ' + email.timestamp + ' ' + email.sender + ' wrote: ' + email.body)
      );

      
      container.appendChild(createParagraphElement(`Sender: ${email.sender}`));
      container.appendChild(createParagraphElement(`Recipients: ${email.recipients.join(', ')}`));
      container.appendChild(createParagraphElement(`Subject: ${email.subject}`));
      container.appendChild(createParagraphElement(`Body: ${email.body}`));
      container.appendChild(createParagraphElement(`Timestamp: ${email.timestamp}`));
      container.appendChild(button);
      email_box.appendChild(container);
  });

  fetch(`emails/${ email_id }`, {
    method: 'PUT',
    body: JSON.stringify({
      read: true,
    })
  })

}

function load_mailbox(mailbox) {

  const view = document.querySelector('#emails-view');
  // Show the mailbox and hide other views
  view.style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';

  // Show the mailbox name
  view.innerHTML = ''
  const header = document.createElement('h3');
  header.innerHTML = mailbox.charAt(0).toUpperCase() + mailbox.slice(1);
  view.appendChild(header); 
  const content = document.createElement('div');
  content.className = 'container mt-4';
  
  
  fetch(`emails/${ mailbox }`)
    .then(response => response.json())
    .then(emails => {
      for (const email of emails){
        const card = document.createElement('div');
        const card_body = document.createElement('div');
        card.className = 'card card-body';
        card.style.backgroundColor = (email.read === true) ? 'lightgrey' : 'white';
        //card.href = 'emails/'+email.id;

        const cardTitle = document.createElement('h5');
        cardTitle.className = 'card-title';
        cardTitle.textContent = 'Subject: ' + email.subject;

        const cardSubtitle = document.createElement('h6');
        cardSubtitle.className = 'card-subtitle mb-2';
        cardSubtitle.textContent = 'From: ' + email.sender;

        const cardText = document.createElement('p');
        cardText.className = 'card-subtitle text-muted';
        cardText.textContent = email.timestamp;

        const archive = document.createElement('button');
        
        archive.innerHTML = (email.archived == false) ? "Archive" : "Unarchive";
        archive.className = 'btn btn-primary';
        archive.addEventListener('click', () => {
          fetch(`emails/${ email.id }`, {
            method: 'PUT',
            body: JSON.stringify({
              archived: !email.archived,
            })
          })
          .then(response => {
            load_mailbox(mailbox)
          }); // solve the issue with not updating the inbox
        });

        card_body.appendChild(cardTitle);
        card_body.appendChild(cardSubtitle);
        card_body.appendChild(cardText);
        card_body.addEventListener('click', () => view_email(email.id));

        card.appendChild(card_body);
        card.appendChild(archive);
        content.appendChild(card);
        
      }
    });
  view.appendChild(content);

}
