<?php include_once('header.php');?>
<div class="container">


<?php echo form_open("welcome/change/{$post->id}",['class'=>'form-horizontal']);?>
   <fieldset>
    <legend>Update Post</legend>
    
   <div class = "form-group">
        <label for="titlename" class="col-md-2 control-lable">Job</label>
       <div class="col-md-5">
         <?php echo form_input(['name'=>'job','placeholder'=>'Job','class'=>'form-control','value'=>set_value('job',$post->job)]);?>
           
       </div>   
          <div class="col-md-5">   
          <?php echo form_error('job','<div class="text-danger">','</div>');?>     
          </div>
   </div>
  
    <div class="form-group">
      <label for="exampleTextarea">Description</label>
      <?php echo form_textarea(['name'=>'description','placeholder'=>'Description','class'=>'form-control','value'=>set_value('description',$post->description)]); ?>
    </div>
     <div class="col-md-5">   
          <?php echo form_error('title','<div class="text-danger">','</div>');?>      
     </div>
      <div class="col-md-5">   
             <input type="date" name="finish_date"  value="<?php echo $post->finish_date; ?>"/>
        </div>
     <?php echo form_submit(['name'=>'submit','value'=>'Update','class'=>'btn btn-primary']); ?>
     <?php echo anchor('welcome','Back',['class'=>'btn btn-default']);?>
   
  </fieldset>
  <?php echo form_close();?>
</div>
