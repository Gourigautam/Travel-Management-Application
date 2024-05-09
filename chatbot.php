<?php
session_start();
if (isset($_SESSION['email']) && isset($_SESSION['name'])){
    $name =$_SESSION['name'];

}else{
    header('location:index.php?error=Please login first!');
}

?>
<html>
  <head>
    <title>TravelsMaxxing</title>
    <link rel="stylesheet" href="styles.css" />
      <script>const d = new Date();
        const  ti= now.toLocaleTimeString([], {hour: '2-digit', minute: '2-digit' });
        var timeee = document.getElementById('timee');
        timeee.innerHTML = ti;
        </script>
    <!-- Import this CDN to use icons -->
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css"
    />
  </head>

  
  <body>
    <!-- Main container -->
    <div class="container">
      <!-- msg-header section starts -->
      <div class="msg-header">
        <div class="container1">
          <img src="download.jpg" class="msgimg" />
          <div class="active">
            <p>TravelsMaxxing</p>
            
          </div>
          
        </div>
      </div>
      <!-- msg-header section ends -->

      <!-- Chat inbox  -->
      <div class="chat-page">
        <div class="msg-inbox" style="height: 45rem;">
          <div class="chats">
            <!-- Message container -->
            <div class="msg-page" style="max-height: 45rem;">
              <!-- Incoming messages -->

              <div class="received-chats">
                <div class="received-chats-img">
                  <img src="OIP.gif" />
                </div>
                <div class="received-msg">
                  <div class="received-msg-inbox">
                    <p>
                     Hi i am  Chico,What can i do for you <?php echo $name; ?>
                    </p>
                    <span class="time"  id="timee" ></span>
                  </div>
                </div>
              </div>

          


              </div>
            </div>
          </div>

          <!-- msg-bottom section -->

          <div class="msg-bottom">
            <div class="input-group">
              <input
                type="text"
                class="form-control"
                placeholder="Write message..."
              />

              <span class="input-group-text send-icon">
                <i class="bi bi-send"></i>
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </body>
  <script src="main.js"></script>
</html>


