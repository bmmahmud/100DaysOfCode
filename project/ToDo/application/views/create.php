<?php include_once('header.php'); ?>
<div class="container">

    <?php echo form_open('welcome/save', ['class' => 'form-horizontal']); ?>
    <fieldset>
        <legend>New Job</legend>

        <div class = "form-group">
            <label for="titlename" class="col-md-2 control-lable">JOB</label>
            <div class="col-md-5">
                <?php echo form_input(['name' => 'job', 'placeholder' => 'Job', 'class' => 'form-control']); ?>
            </div>   
            <div class="col-md-5">   
                <?php echo form_error('job', '<div class="text-danger">', '</div>'); ?>     
            </div>
        </div>

        <div class="form-group">
            <label for="exampleTextarea">Description</label>
            <?php echo form_textarea(['name' => 'description', 'placeholder' => 'Description', 'class' => 'form-control']); ?>
        </div>
        <div class="col-md-5">   
            <?php echo form_error('title', '<div class="text-danger">', '</div>'); ?>      
        </div>
        <div class="col-md-5">   
               <input type="date" name="finish_date"><br><br>
        </div>
     
        <?php echo form_submit(['name' => 'submit', 'value' => 'Submit', 'class' => 'btn btn-primary']); ?>
        <?php echo anchor('welcome', 'Back', ['class' => 'btn btn-default']); ?>

    </fieldset>
    <?php echo form_close(); ?>
</div>

