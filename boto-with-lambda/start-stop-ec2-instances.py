import boto3

def lambda_handler(event, context):
    
    # get list of regions in AWS
    ec2 = boto3.client('ec2')
    
    # grab regions
    regions = [region['RegionName']
                for region in ec2.describe_regions()['Regions']]
                
    # iterate through list
    for region in regions:
        ec2_res = boto3.resource('ec2', region_name=region)
        
        print('Region', region)
        
        # get only running instances
        instances = ec2_res.instances.filter(
            Filters=[{
                'Name': 'instance-state-name',
                'Values': ['running']}])
        
        # stop the instances
        for instance in instances:
            instance.stop()
            
            print('Stopped instance: ', instance.id )