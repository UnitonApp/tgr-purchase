<?php
function create_order($currency, $payment_system, $fields, $items) {
    $python_script_path = '../../../python/integration.py';
    $output = shell_exec('python ' . $python_script_path . $currency . $payment_system . $fields . $items);
    return $output;
}
?>
