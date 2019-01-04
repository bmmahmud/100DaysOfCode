<?php include_once('header.php'); ?>

<!-- Table -->
<div class="container">

    <h3>View All Posts:</h3>
    <!-- Button Action Message -->
    <?php if ($msg = $this->session->flashdata('msg')): ?>
        <?php echo $msg; ?>
    <?php endif; ?>

    <!-- Button Action Message -->
    <?php echo anchor('welcome/create', 'ADD ToDo', array('class' => 'btn btn-primary')); ?>

    
    <!-- Table -->
    <table class="table table-hover">
        <thead>
            <tr>
                <th scope="col">Job</th>
                <th scope="col">Description</th>
                <th scope="col">Created Dated</th>
                <th scope="col">Finish Date</th>
                <th scope="col">Active</th>
            </tr>
        </thead>


        <tr class="table-secondary">
        <tbody>
            <?php if (count($post)): ?>
                <?php foreach ($post as $posts): ?>
                    <tr>
                        <td><?php echo $posts->job; ?></td>
                        <td><?php echo $posts->description; ?></td>
                        <td><?php echo $posts->created_date; ?></td>
                         <td><?php echo $posts->finish_date; ?></td>

                        <td>
                            <?php echo anchor("welcome/view/{$posts->id}", 'View', array('class' => 'badge badge-primary')); ?>
                            <?php echo anchor("welcome/update/{$posts->id}", 'Update', array('class' => 'badge badge-success')); ?>
                            <?php echo anchor("welcome/delete/{$posts->id}", 'Delete', array('class' => 'badge badge-danger')); ?>
                        </td>
                    </tr> 
                <?php endforeach; ?>

            <?php else: ?>
                <tr>
                    <td>No record found</td>
                </tr>

            <?php endif; ?> 
        </tbody>
        </tr>
    </table> 

</div>

</body>
</html>